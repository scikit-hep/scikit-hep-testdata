from __future__ import annotations

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
    def dummy_remote_file(filename, data_dir=None, raise_missing=False):
        if not data_dir:
            data_dir = str(tmpdir)
        return str(Path(data_dir) / filename)

    monkeypatch.setattr(skhtd.remote_files, "remote_file", dummy_remote_file)
    monkeypatch.setattr(skhtd.remote_files, "is_known_remote", lambda _: True)

    path = skhtd.data_path(str(Path("dataset") / "a_remote_file.root"))
    assert path == str(tmpdir / "dataset" / "a_remote_file.root")
