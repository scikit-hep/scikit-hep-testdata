# -*- coding: utf-8 -*-
import os

import skhep_testdata as skhtd

_remote_dataset_cfg = os.path.join(
    os.path.dirname(__file__), "test_remote_datasets.yml"
)
skhtd.remote_files.RemoteDatasetList.load_remote_configs(_remote_dataset_cfg)

good_file_1 = os.path.join("dataset_1", "file_1.root")
bad_file_1 = os.path.join("bad_dataset_1", "file_1.root")


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


def test_remote_file(tmpdir, monkeypatch):
    def fake_urlretrieve(url, writefile):
        with open(writefile, "w") as outfile:
            outfile.write("testing...")

    monkeypatch.setattr(skhtd.remote_files, "urlretrieve", fake_urlretrieve)

    path = skhtd.remote_files.remote_file(good_file_1, data_dir=str(tmpdir))
    assert path == str(tmpdir / "dataset_1" / "file_1.root")
