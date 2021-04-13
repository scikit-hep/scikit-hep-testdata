# -*- coding: utf-8 -*-
from __future__ import absolute_import

import atexit
import sys

from . import remote_files

if sys.version_info < (3, 9):
    import importlib_resources as resources
    from importlib_resources import as_file
else:
    from importlib import resources
    from importlib.resources import as_file

if sys.version_info < (3, 3):
    from contextlib2 import ExitStack
else:
    from contextlib import ExitStack


def data_path(filename, raise_missing=True):
    # type: (str, bool) -> str
    if remote_files.is_known_remote(filename):
        return remote_files.remote_file(filename, raise_missing=raise_missing)

    ref = resources.files("skhep_testdata.data") / filename
    file_manager = ExitStack()
    atexit.register(file_manager.close)
    file_path = file_manager.enter_context(as_file(ref))
    if raise_missing and not file_path.exists():
        raise RuntimeError("Unknown or missing file: {}".format(filename))
    return str(file_path)
