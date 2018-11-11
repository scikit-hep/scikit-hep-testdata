import pytest
import os
import skhep_testdata as skhtd


data_dir = os.path.dirname(skhtd.__file__)
data_dir = os.path.join(data_dir, "data")


def test_data_path():
    path = os.path.join(data_dir, "uproot-Zmumu.root")
    assert skhtd.data_path("uproot-Zmumu.root") == path


def test_data_path_missing():
    path = skhtd.data_path("doesnt-exist.root", raise_missing=False)
    assert path == os.path.join(data_dir, "doesnt-exist.root")

    with pytest.raises(RuntimeError):
        skhtd.data_path("doesnt-exist.root")

    with pytest.raises(RuntimeError):
        skhtd.data_path("doesnt-exist.root", raise_missing=True)


def test_delegate_to_remore(monkeypatch):
    def dummy_remote_file(*args, **kwargs):
        return "called dummy_remote_file"

    monkeypatch.setattr(skhtd.remote_files, "remote_file", dummy_remote_file)
    monkeypatch.setattr(skhtd.remote_files, "is_known_remote", lambda x: True)

    path = skhtd.data_path("dataset/a_remote_file.root")
    assert path == "called dummy_remote_file"
