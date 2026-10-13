from __future__ import annotations

from pathlib import Path

import skhep_testdata as skhtd


def test_cache_path_default(isolated_home):
    expected = isolated_home / ".local" / "skhepdata"
    assert not expected.exists()
    assert skhtd.data.cache_path() == expected
    assert expected.is_dir()


def test_cache_path_explicit(tmp_path):
    assert skhtd.data.cache_path(str(tmp_path)) == tmp_path
    assert skhtd.data.cache_path(tmp_path / "x") == tmp_path / "x"
    # An explicit cache_dir is used as-is
    assert not Path(tmp_path / "x").exists()
