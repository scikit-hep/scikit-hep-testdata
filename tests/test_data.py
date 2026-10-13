from __future__ import annotations

import pytest

import skhep_testdata as skhtd


def test_cache_path_default(isolated_home):
    expected = isolated_home / ".local" / "skhepdata"
    assert not expected.exists()
    assert skhtd.data.cache_path() == expected
    assert expected.is_dir()


def test_cache_path_explicit(tmp_path):
    assert skhtd.data.cache_path(str(tmp_path)) == tmp_path
    # A cache_dir that doesn't exist yet is created, like the default one
    expected = tmp_path / "x" / "y"
    assert skhtd.data.cache_path(expected) == expected
    assert expected.is_dir()


def test_atomic_write(tmp_path):
    target = tmp_path / "file.root"
    with skhtd.data.atomic_write(target) as f:
        f.write(b"partial")
        # Nothing is visible under the final name until the write completes
        assert not target.exists()
        f.write(b" and complete")

    assert target.read_bytes() == b"partial and complete"
    assert sorted(p.name for p in tmp_path.iterdir()) == ["file.root"]


def write_then_fail(path):
    with skhtd.data.atomic_write(path) as f:
        f.write(b"partial")
        raise ConnectionError


def test_atomic_write_interrupted(tmp_path):
    target = tmp_path / "file.root"
    with pytest.raises(ConnectionError):
        write_then_fail(target)

    assert list(tmp_path.iterdir()) == []


def test_atomic_write_interrupted_keeps_existing(tmp_path):
    target = tmp_path / "file.root"
    target.write_bytes(b"old")
    with pytest.raises(ConnectionError):
        write_then_fail(target)

    assert target.read_bytes() == b"old"
    assert sorted(p.name for p in tmp_path.iterdir()) == ["file.root"]
