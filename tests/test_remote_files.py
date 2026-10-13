from __future__ import annotations

import io
import tarfile
from pathlib import Path

import pytest
import requests

import skhep_testdata as skhtd

RemoteDatasetList = skhtd.remote_files.RemoteDatasetList

good_file_1 = str(Path("dataset_1") / "file_1.root")
good_file_2 = str(Path("dataset_2") / "file_2.root")
good_file_3 = str(Path("dataset_3") / "file_3.root")
bad_file_1 = str(Path("bad_dataset_1") / "file_1.root")


def make_tar(members):
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w") as tar:
        for name, content in members.items():
            info = tarfile.TarInfo(name)
            info.size = len(content)
            tar.addfile(info, io.BytesIO(content))
    return buffer.getvalue()


class FakeResponse:
    def __init__(self, content):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def raise_for_status(self):
        pass

    def iter_content(self, chunk_size):
        for i in range(0, len(self.content), chunk_size):
            yield self.content[i : i + chunk_size]


@pytest.fixture
def fake_get(monkeypatch):
    """Serve ``fake_get.content`` for any URL and record the requests made."""

    def get(url, stream=False, timeout=None):
        get.calls.append((url, stream, timeout))
        return FakeResponse(get.content)

    get.calls = []
    get.content = b""
    monkeypatch.setattr(skhtd.remote_files.requests, "get", get)
    return get


@pytest.fixture
def no_network(monkeypatch):
    def get(*args, **kwargs):
        msg = "unexpected download"
        raise AssertionError(msg)

    monkeypatch.setattr(skhtd.remote_files.requests, "get", get)


def test_bundled_remote_datasets():
    for name in ("data", "dy", "qcd", "single_top", "ttbar", "wjets", "ww", "wz", "zz"):
        assert skhtd.remote_files.is_known_remote(f"cms_hep_2012_tutorial/{name}.root")
    assert not skhtd.remote_files.is_known_remote("cms_hep_2012_tutorial/HEPTutorial")


@pytest.mark.usefixtures("test_remote_configs")
def test_is_known_remote():
    assert skhtd.remote_files.is_known_remote(good_file_1)
    assert skhtd.remote_files.is_known_remote(good_file_2)
    assert not skhtd.remote_files.is_known_remote(bad_file_1)
    # Dict-style entries are keyed by the output name, not the path in the archive
    assert not skhtd.remote_files.is_known_remote("dataset_2/subdir/inner_2.root")


@pytest.mark.usefixtures("test_remote_configs")
def test_get_config_for_file():
    config = RemoteDatasetList.get_config_for_file(good_file_1)
    assert config == {
        "dataset_name": "dataset_1",
        "url": "http://not-a-real-url.com/dataset_1.tar",
        "files": {"file_1.root": "file_1.root"},
    }

    # Callers add keys to the returned config, so it must not alias the cache
    config["cache_dir"] = "somewhere"
    assert "cache_dir" not in RemoteDatasetList.get_config_for_file(good_file_1)


@pytest.mark.usefixtures("test_remote_configs")
def test_get_config_for_unknown_file():
    with pytest.raises(RuntimeError, match="Unknown remote file"):
        RemoteDatasetList.get_config_for_file(bad_file_1)


def test_make_dirs(tmp_path):
    path = tmp_path / "subdir_1" / "another_subdir"
    skhtd.remote_files.make_all_dirs(str(path))
    assert path.is_dir()
    # Creating it again is a no-op
    skhtd.remote_files.make_all_dirs(str(path))
    assert path.is_dir()


@pytest.mark.usefixtures("test_remote_configs")
def test_remote_file_extracts_tar(tmp_path, fake_get):
    fake_get.content = make_tar({"file_1.root": b"one", "unlisted.root": b"nope"})

    path = skhtd.remote_files.remote_file(good_file_1, cache_dir=str(tmp_path))

    assert path == str(tmp_path / "dataset_1" / "file_1.root")
    assert Path(path).read_bytes() == b"one"
    assert fake_get.calls == [("http://not-a-real-url.com/dataset_1.tar", True, 30)]
    # Only the listed members are extracted
    assert not (tmp_path / "dataset_1" / "unlisted.root").exists()


@pytest.mark.usefixtures("test_remote_configs")
def test_remote_file_renames_tar_members(tmp_path, fake_get):
    fake_get.content = make_tar({"subdir/inner_2.root": b"two"})

    path = skhtd.remote_files.remote_file(good_file_2, cache_dir=str(tmp_path))

    assert path == str(tmp_path / "dataset_2" / "file_2.root")
    assert Path(path).read_bytes() == b"two"
    assert not (tmp_path / "dataset_2" / "subdir" / "inner_2.root").exists()


@pytest.mark.usefixtures("test_remote_configs")
def test_remote_file_not_a_tar(tmp_path, fake_get):
    fake_get.content = b"root file contents"

    path = skhtd.remote_files.remote_file(good_file_3, cache_dir=str(tmp_path))

    assert path == str(tmp_path / "dataset_3" / "file_3.root")
    assert Path(path).read_bytes() == b"root file contents"


@pytest.mark.usefixtures("test_remote_configs")
def test_remote_file_default_cache_dir(isolated_home, fake_get):
    fake_get.content = b"root file contents"

    path = skhtd.remote_files.remote_file(good_file_3)

    expected = isolated_home / ".local" / "skhepdata" / "dataset_3" / "file_3.root"
    assert path == str(expected)
    assert expected.read_bytes() == b"root file contents"


@pytest.mark.usefixtures("test_remote_configs")
def test_remote_file_interrupted_download(tmp_path, monkeypatch, fake_get):
    class InterruptedResponse(FakeResponse):
        def iter_content(self, chunk_size):  # noqa: ARG002
            yield self.content[:10]
            raise requests.ConnectionError

    def interrupted_get(url, stream=False, timeout=None):
        return InterruptedResponse(make_tar({"file_1.root": b"one"}))

    monkeypatch.setattr(skhtd.remote_files.requests, "get", interrupted_get)
    with pytest.raises(requests.ConnectionError):
        skhtd.remote_files.remote_file(good_file_1, cache_dir=str(tmp_path))

    # No partial archive is left behind to be mistaken for a complete one
    assert list((tmp_path / "dataset_1").iterdir()) == []

    # So the next attempt downloads it again
    monkeypatch.setattr(skhtd.remote_files.requests, "get", fake_get)
    fake_get.content = make_tar({"file_1.root": b"one"})
    path = skhtd.remote_files.remote_file(good_file_1, cache_dir=str(tmp_path))
    assert Path(path).read_bytes() == b"one"
    assert len(fake_get.calls) == 1


@pytest.mark.usefixtures("test_remote_configs", "no_network")
def test_remote_file_already_cached(tmp_path):
    cached = tmp_path / "dataset_1" / "file_1.root"
    cached.parent.mkdir()
    cached.write_bytes(b"cached")

    path = skhtd.remote_files.remote_file(good_file_1, cache_dir=str(tmp_path))
    assert path == str(cached)


@pytest.mark.usefixtures("test_remote_configs", "no_network")
def test_remote_file_archive_already_downloaded(tmp_path):
    # e.g. the extracted file was deleted from the cache: re-extract it from
    # the archive that is already there instead of downloading it again
    archive = tmp_path / "dataset_2" / "dataset_2.tar"
    archive.parent.mkdir()
    archive.write_bytes(make_tar({"subdir/inner_2.root": b"two"}))

    path = skhtd.remote_files.remote_file(good_file_2, cache_dir=str(tmp_path))
    assert path == str(tmp_path / "dataset_2" / "file_2.root")
    assert Path(path).read_bytes() == b"two"


@pytest.mark.usefixtures("test_remote_configs")
def test_remote_file_missing(tmp_path, fake_get):
    # The download succeeds but does not contain the requested file
    fake_get.content = b"not a tarball"

    path = skhtd.remote_files.remote_file(good_file_1, cache_dir=str(tmp_path))
    assert path == str(tmp_path / "dataset_1" / "file_1.root")
    assert not Path(path).exists()

    with pytest.raises(RuntimeError, match="cannot be found"):
        skhtd.remote_files.remote_file(
            good_file_1, cache_dir=str(tmp_path), raise_missing=True
        )
