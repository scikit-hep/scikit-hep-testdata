# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys
import tempfile
import typing
import zipfile
from typing import Any, Optional

import requests

from . import data, remote_files

if sys.version_info < (3, 5):
    from pathlib2 import Path
else:
    from pathlib import Path

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources

__all__ = ("data_path", "download_all", "known_files")


DIR = Path(__file__).parent.resolve()

baseurl = "https://raw.githubusercontent.com/scikit-hep/scikit-hep-testdata/main/src/skhep_testdata/data/"
zipurl = "https://github.com/scikit-hep/scikit-hep-testdata/zipball/main"


with resources.as_file(resources.files(data) / "file_list.txt") as fp, fp.open() as f:
    known_files = {n.strip() for n in f if n.strip()}


def _cache_path(cache_dir=None):
    # type: (Optional[str]) -> Path
    if cache_dir is None:
        skhepdir = Path.home() / ".local" / "skhepdata"
        # But in typeshed - https://github.com/python/typeshed/pull/5218
        if sys.version_info < (3, 5):
            typing.cast(Any, skhepdir.mkdir)(exist_ok=True, parents=True)
        else:
            skhepdir.mkdir(exist_ok=True, parents=True)
        return skhepdir
    else:
        return Path(cache_dir)


def data_path(filename, raise_missing=True, cache_dir=None):
    # type: (str, bool, Optional[str]) -> str
    if remote_files.is_known_remote(filename):
        return remote_files.remote_file(filename, raise_missing=raise_missing)

    if filename not in known_files and raise_missing:
        if sys.version_info < (3,):
            raise IOError(filename)
        else:
            raise FileNotFoundError(filename)

    filepath = DIR / "data" / filename

    if not filepath.exists() and filename in known_files:
        cached_path = _cache_path(cache_dir) / filename

        if not cached_path.exists():
            # Currently get from main branch
            # Could locally cache if not fixable, or always cache locally
            # Could verify exists first
            # Download all not implemented
            response = requests.get(baseurl + filename)
            response.raise_for_status()
            with cached_path.open("wb") as f:
                f.write(response.content)
        return str(cached_path)

    return str(filepath)


def download_all(cache_dir=None):
    # type: (Optional[str]) -> None
    local_dir = _cache_path(cache_dir)

    with tempfile.TemporaryFile() as f:
        with requests.get(zipurl, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        with zipfile.ZipFile(f) as z:
            for n in z.namelist():
                if "src/skhep_testdata/data/" in n and not n.endswith(".py"):
                    z.extract(n, str(local_dir / str(n.split("/")[-1])))
