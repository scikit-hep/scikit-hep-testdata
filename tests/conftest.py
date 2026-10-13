from __future__ import annotations

from pathlib import Path

import pytest

import skhep_testdata as skhtd

TEST_REMOTE_CONFIG = str(Path(__file__).parent / "test_remote_datasets.yml")


@pytest.fixture(autouse=True)
def isolated_home(monkeypatch, tmp_path_factory):
    """Keep the default cache dir (~/.local/skhepdata) out of the real home."""
    home = tmp_path_factory.mktemp("home")
    monkeypatch.setattr(Path, "home", lambda: home)
    return home


@pytest.fixture(autouse=True)
def clean_remote_configs():
    """Start each test with an empty remote dataset cache, then restore it."""
    all_files = skhtd.remote_files.RemoteDatasetList._all_files
    saved = dict(all_files)
    all_files.clear()
    yield
    all_files.clear()
    all_files.update(saved)


@pytest.fixture
def test_remote_configs():
    skhtd.remote_files.RemoteDatasetList.load_remote_configs(TEST_REMOTE_CONFIG)
