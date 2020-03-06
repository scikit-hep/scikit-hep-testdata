from __future__ import absolute_import

import os

from . import remote_files

# We are using the new files interface, which *probably* will be in Python
# 3.9's importlib.resources. Let's be sure to use the package for now:
import importlib_resources

try:
    from importlib_resources import as_file
except ImportError:
    from importlib_resources.trees import as_file

try:
    from contextlib import ExitStack
except ImportError:
    from contextlib2 import ExitStack

import atexit


def data_path(filename, raise_missing=True):
    if remote_files.is_known_remote(filename):
        return remote_files.remote_file(filename, raise_missing=raise_missing)

    ref = importlib_resources.files("skhep_testdata.data") / filename
    file_manager = ExitStack()
    atexit.register(file_manager.close)
    file_path = file_manager.enter_context(as_file(ref))
    if raise_missing and not file_path.exists():
            raise RuntimeError("Unknown or missing file: {0}".format(filename))
    return str(file_path)
