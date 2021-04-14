# -*- coding: utf-8 -*-
from __future__ import absolute_import

from typing import Tuple

from .local_files import data_path, download_all, known_files
from .version import version as __version__

__all__ = ("data_path", "download_all", "known_files", "__version__")


def __dir__():
    # type: () -> Tuple[str, ...]
    return __all__
