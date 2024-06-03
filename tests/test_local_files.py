from __future__ import annotations

import os

import pytest
import requests

import skhep_testdata as skhtd

data_dir = os.path.dirname(skhtd.__file__)
data_dir = os.path.join(data_dir, "data")


def test_data_path():
    assert os.path.exists(skhtd.data_path("uproot-Zmumu.root"))


def test_data_path_missing():
    path = skhtd.data_path("doesnt-exist.root", raise_missing=False)
    assert path == os.path.join(data_dir, "doesnt-exist.root")

    with pytest.raises(IOError):
        skhtd.data_path("doesnt-exist.root")

    with pytest.raises(IOError):
        skhtd.data_path("doesnt-exist.root", raise_missing=True)


def test_data_path_cached():
    skhtd.known_files.add("dummy-cached.root")
    with pytest.raises(requests.exceptions.HTTPError):
        skhtd.data_path("dummy-cached.root", raise_missing=False, cache_dir="tmp")


def test_delegate_to_remote(monkeypatch, tmpdir):
    def dummy_remote_file(filename, data_dir=None, raise_missing=False):
        if not data_dir:
            data_dir = str(tmpdir)
        return os.path.join(data_dir, filename)

    monkeypatch.setattr(skhtd.remote_files, "remote_file", dummy_remote_file)
    monkeypatch.setattr(skhtd.remote_files, "is_known_remote", lambda _: True)

    path = skhtd.data_path(os.path.join("dataset", "a_remote_file.root"))
    assert path == str(tmpdir / "dataset" / "a_remote_file.root")
