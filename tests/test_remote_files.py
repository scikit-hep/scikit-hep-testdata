from __future__ import annotations

from pathlib import Path

import skhep_testdata as skhtd

_remote_dataset_cfg = str(Path(__file__).parent / "test_remote_datasets.yml")
skhtd.remote_files.RemoteDatasetList.load_remote_configs(_remote_dataset_cfg)

good_file_1 = str(Path("dataset_1") / "file_1.root")
bad_file_1 = str(Path("bad_dataset_1") / "file_1.root")


def test_is_known_remote():
    assert skhtd.remote_files.is_known_remote(good_file_1)
    assert not skhtd.remote_files.is_known_remote(bad_file_1)


def test_get_config_for_file():
    config = skhtd.remote_files.RemoteDatasetList.get_config_for_file(good_file_1)
    assert config["dataset_name"] == "dataset_1"
    assert config["url"] == "http://not-a-real-url.com/dataset_1.tar"


def test_make_dirs(tmpdir):
    tmppath = str(tmpdir / "subdir_1" / "another_subdir")
    # Create the directory
    skhtd.remote_files.make_all_dirs(tmppath)
    # Create the directory again, which should pass unchecked
    skhtd.remote_files.make_all_dirs(tmppath)


class FakeResponse:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def raise_for_status(self):
        pass

    def iter_content(self, chunk_size):  # noqa: ARG002
        yield b"testing..."


def test_remote_file(tmpdir, monkeypatch):
    def fake_get(url, stream=False, timeout=None):
        return FakeResponse()

    monkeypatch.setattr(skhtd.remote_files.requests, "get", fake_get)

    path = skhtd.remote_files.remote_file(good_file_1, cache_dir=str(tmpdir))
    assert path == str(tmpdir / "dataset_1" / "file_1.root")
