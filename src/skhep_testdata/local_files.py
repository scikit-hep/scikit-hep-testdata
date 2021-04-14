# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys

import requests

from . import data, remote_files

if sys.version_info < (3,):
    from pathlib2 import Path
else:
    from pathlib import Path

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources

DIR = Path(__file__).parent.resolve()

baseurl = "https://raw.githubusercontent.com/scikit-hep/scikit-hep-testdata/master/src/skhep_testdata/data/"


with resources.as_file(resources.files(data) / "file_list.txt") as fp, fp.open() as f:
    known_files = {n.strip() for n in f if n.strip()}


def data_path(filename, raise_missing=True):
    # type: (str, bool) -> str
    if remote_files.is_known_remote(filename):
        return remote_files.remote_file(filename, raise_missing=raise_missing)

    if filename not in known_files and raise_missing:
        if sys.version_info < (3,):
            raise IOError(filename)
        else:
            raise FileNotFoundError(filename)

    filepath = DIR / "data" / filename

    if not filepath.exists() and filename in known_files:
        skhepdir = Path.home() / ".local" / "skhepdata"
        skhepdir.mkdir(exist_ok=True, parents=True)
        cached_path = skhepdir / filename
        if not cached_path.exists():
            # Currently get from master branch
            # Could locally cache if not fixable, or always cache locally
            # Could verify exists first
            # Download all not implemented
            response = requests.get(baseurl + filename)
            response.raise_for_status()
            with cached_path.open("wb") as f:
                f.write(response.content)
        return str(cached_path)

    return str(filepath)
