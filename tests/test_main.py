from __future__ import annotations

import sys

import pytest

import skhep_testdata as skhtd
from skhep_testdata import __main__


@pytest.fixture
def run(monkeypatch, capsys):
    def run(*args):
        monkeypatch.setattr(sys, "argv", ["skhep_testdata", *args])
        __main__.main()
        return capsys.readouterr().out.splitlines()

    return run


@pytest.fixture
def fake_data_path(monkeypatch):
    calls = []

    def data_path(filename, cache_dir=None):
        calls.append((filename, cache_dir))
        return f"/expanded/{filename}"

    monkeypatch.setattr(__main__, "data_path", data_path)
    return calls


@pytest.fixture
def fake_download_all(monkeypatch):
    calls = []
    monkeypatch.setattr(__main__, "download_all", calls.append)
    return calls


def test_no_args(run, fake_data_path, fake_download_all):
    assert run() == []
    assert fake_data_path == []
    assert fake_download_all == []


def test_list(run):
    assert run("--list") == sorted(skhtd.known_files)


def test_all(run, fake_download_all):
    assert run("--all") == []
    assert fake_download_all == [None]


def test_all_dir(run, fake_download_all):
    run("--all", "--dir", "somewhere")
    assert fake_download_all == ["somewhere"]


def test_file_paths(run, fake_data_path):
    assert run("a.root", "b/c.root") == ["/expanded/a.root", "/expanded/b/c.root"]
    assert fake_data_path == [("a.root", None), ("b/c.root", None)]


def test_file_paths_dir(run, fake_data_path):
    # Regression test: --dir used to be passed as raise_missing (#226)
    assert run("--dir", "somewhere", "a.root") == ["/expanded/a.root"]
    assert fake_data_path == [("a.root", "somewhere")]


def test_missing_file(run):
    with pytest.raises(FileNotFoundError, match=r"doesnt-exist\.root"):
        run("doesnt-exist.root")
