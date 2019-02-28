from __future__ import absolute_import

import os

from . import remote_files


__top_directory__ = os.path.realpath(os.path.dirname(__file__))
__data_directory__ = os.path.join(__top_directory__, "data")


def data_path(filename, raise_missing=True):
    path = os.path.join(__data_directory__, filename)
    if os.path.isfile(path):
        return path

    if remote_files.is_known_remote(filename):
        return remote_files.remote_file(filename, raise_missing=raise_missing)

    if raise_missing:
        raise RuntimeError("Unknown or missing file: %s" % filename)

    return None
