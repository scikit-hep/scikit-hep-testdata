from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pytest
import requests

import skhep_testdata as skhtd

data_dir = Path(skhtd.__file__).parent / "data"


class FakeResponse:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def raise_for_status(self):
        pass

    def iter_content(self, chunk_size=8192):
        for i in range(0, len(self.content), chunk_size):
            yield self.content[i : i + chunk_size]


@pytest.fixture
def dummy_known_file(monkeypatch):
    """A known file that is not present in the package data directory."""
    filename = "dummy-cached.root"
    monkeypatch.setattr(
        skhtd.local_files, "known_files", skhtd.known_files | {filename}
    )
    return filename


@pytest.fixture
def no_network(monkeypatch):
    def get(*args, **kwargs):
        msg = "unexpected download"
        raise AssertionError(msg)

    monkeypatch.setattr(skhtd.local_files.requests, "get", get)


def test_known_files():
    assert "uproot-Zmumu.root" in skhtd.known_files
    # Only data files are listed, not the package's own files
    assert not any(n.endswith((".py", ".txt")) for n in skhtd.known_files)


def test_data_path():
    # Either packaged locally or downloaded from GitHub, depending on the install
    path = Path(skhtd.data_path("uproot-Zmumu.root"))
    assert path.is_absolute()
    assert path.name == "uproot-Zmumu.root"
    with path.open("rb") as f:
        assert f.read(4) == b"root"


def test_data_path_missing():
    path = skhtd.data_path("doesnt-exist.root", raise_missing=False)
    assert path == str(data_dir / "doesnt-exist.root")

    with pytest.raises(FileNotFoundError, match=r"doesnt-exist\.root"):
        skhtd.data_path("doesnt-exist.root")


def test_data_path_download(monkeypatch, isolated_home, dummy_known_file):
    calls = []

    def fake_get(url, timeout):
        calls.append((url, timeout))
        return FakeResponse(b"downloaded")

    monkeypatch.setattr(skhtd.local_files.requests, "get", fake_get)

    path = skhtd.data_path(dummy_known_file)

    expected = isolated_home / ".local" / "skhepdata" / dummy_known_file
    assert path == str(expected)
    assert expected.read_bytes() == b"downloaded"
    assert calls == [(skhtd.local_files.baseurl + dummy_known_file, 30)]


def test_data_path_new_cache_dir(monkeypatch, tmp_path, dummy_known_file):
    monkeypatch.setattr(
        skhtd.local_files.requests,
        "get",
        lambda *a, **k: FakeResponse(b"downloaded"),
    )
    cache_dir = tmp_path / "does" / "not" / "exist"

    path = skhtd.data_path(dummy_known_file, cache_dir=str(cache_dir))

    assert path == str(cache_dir / dummy_known_file)
    assert (cache_dir / dummy_known_file).read_bytes() == b"downloaded"


@pytest.mark.usefixtures("no_network")
def test_data_path_cached(tmp_path, dummy_known_file):
    cached = tmp_path / dummy_known_file
    cached.write_bytes(b"cached")

    path = skhtd.data_path(dummy_known_file, cache_dir=str(tmp_path))
    assert path == str(cached)
    assert cached.read_bytes() == b"cached"


def test_data_path_download_error(monkeypatch, tmp_path, dummy_known_file):
    response = requests.Response()
    response.status_code = 404
    response.reason = "Not Found"
    response.url = skhtd.local_files.baseurl + dummy_known_file

    monkeypatch.setattr(skhtd.local_files.requests, "get", lambda *a, **k: response)
    with pytest.raises(requests.exceptions.HTTPError, match="404") as exc_info:
        skhtd.data_path(dummy_known_file, cache_dir=str(tmp_path))

    assert exc_info.value.response is response
    assert not (tmp_path / dummy_known_file).exists()


def test_data_path_interrupted_download(monkeypatch, tmp_path, dummy_known_file):
    class InterruptedResponse:
        def raise_for_status(self):
            pass

        @property
        def content(self):
            raise requests.ConnectionError

    monkeypatch.setattr(
        skhtd.local_files.requests, "get", lambda *a, **k: InterruptedResponse()
    )
    with pytest.raises(requests.ConnectionError):
        skhtd.data_path(dummy_known_file, cache_dir=str(tmp_path))

    assert list(tmp_path.iterdir()) == []


@pytest.mark.usefixtures("no_network")
def test_data_path_remote(tmp_path):
    # Scoped names from remote_datasets.yml go through remote_files
    cached = tmp_path / "cms_hep_2012_tutorial" / "data.root"
    cached.parent.mkdir()
    cached.write_bytes(b"cached")

    path = skhtd.data_path("cms_hep_2012_tutorial/data.root", cache_dir=str(tmp_path))
    assert path == str(cached)


def test_data_path_remote_forwards_args(monkeypatch):
    calls = []

    def fake_remote_file(filename, cache_dir=None, raise_missing=False):
        calls.append((filename, cache_dir, raise_missing))
        return "remote-path"

    monkeypatch.setattr(skhtd.remote_files, "remote_file", fake_remote_file)

    filename = "cms_hep_2012_tutorial/data.root"
    assert skhtd.data_path(filename) == "remote-path"
    assert skhtd.data_path(filename, raise_missing=False, cache_dir="dir") == (
        "remote-path"
    )
    assert calls == [(filename, None, True), (filename, "dir", False)]


def test_download_all(monkeypatch, tmp_path):
    file_bytes = b"\x90root-file-contents\x00"

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as z:
        z.writestr("repo-abc123/", b"")  # directory entry, must be ignored
        z.writestr("repo-abc123/src/skhep_testdata/data/somefile.root", file_bytes)
        z.writestr("repo-abc123/src/skhep_testdata/data/__init__.py", b"# ignore me")
        z.writestr("repo-abc123/src/skhep_testdata/remote_datasets.yml", b"a: b")
        z.writestr("repo-abc123/dev/make-root/other.root", b"not package data")
    zip_bytes = buffer.getvalue()

    calls = []

    def fake_get(url, stream=False, timeout=None):
        calls.append((url, stream, timeout))
        return FakeResponse(zip_bytes)

    monkeypatch.setattr(skhtd.local_files.requests, "get", fake_get)

    # The cache dir is created if needed
    cache_dir = tmp_path / "new-cache"
    skhtd.download_all(cache_dir=str(cache_dir))

    assert calls == [(skhtd.local_files.zipurl, True, 30)]
    assert sorted(p.name for p in cache_dir.iterdir()) == ["somefile.root"]
    assert (cache_dir / "somefile.root").read_bytes() == file_bytes
