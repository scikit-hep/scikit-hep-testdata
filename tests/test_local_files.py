from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pytest
import requests

import skhep_testdata as skhtd

data_dir = Path(skhtd.__file__).parent / "data"


def test_data_path():
    assert Path(skhtd.data_path("uproot-Zmumu.root")).exists()


def test_data_path_missing():
    path = skhtd.data_path("doesnt-exist.root", raise_missing=False)
    assert path == str(data_dir / "doesnt-exist.root")

    with pytest.raises(IOError):
        skhtd.data_path("doesnt-exist.root")

    with pytest.raises(IOError):
        skhtd.data_path("doesnt-exist.root", raise_missing=True)


def test_data_path_cached():
    skhtd.known_files.add("dummy-cached.root")
    with pytest.raises(requests.exceptions.HTTPError):
        skhtd.data_path("dummy-cached.root", raise_missing=False, cache_dir="tmp")


def test_delegate_to_remote(monkeypatch, tmpdir):
    def dummy_remote_file(filename, cache_dir=None, raise_missing=False):
        if not cache_dir:
            cache_dir = str(tmpdir)
        return str(Path(cache_dir) / filename)

    monkeypatch.setattr(skhtd.remote_files, "remote_file", dummy_remote_file)
    monkeypatch.setattr(skhtd.remote_files, "is_known_remote", lambda _: True)

    path = skhtd.data_path(str(Path("dataset") / "a_remote_file.root"))
    assert path == str(tmpdir / "dataset" / "a_remote_file.root")


def test_download_all(monkeypatch, tmp_path):
    file_bytes = b"\x90root-file-contents\x00"

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as z:
        z.writestr("repo-abc123/", b"")  # directory entry, must be ignored
        z.writestr("repo-abc123/src/skhep_testdata/data/somefile.root", file_bytes)
        z.writestr("repo-abc123/src/skhep_testdata/data/__init__.py", b"# ignore me")
    zip_bytes = buffer.getvalue()

    class DummyResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def raise_for_status(self):
            pass

        def iter_content(self, chunk_size=8192):
            for i in range(0, len(zip_bytes), chunk_size):
                yield zip_bytes[i : i + chunk_size]

    monkeypatch.setattr(
        skhtd.local_files.requests, "get", lambda *a, **k: DummyResponse()
    )

    skhtd.download_all(cache_dir=str(tmp_path))

    extracted = tmp_path / "somefile.root"
    assert extracted.is_file()
    assert extracted.read_bytes() == file_bytes
    assert not (tmp_path / "__init__.py").exists()
