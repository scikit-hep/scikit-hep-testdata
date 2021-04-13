# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .local_files import data_path
from .version import version as __version__

__all__ = ("data_path", "__version__")


def __dir__():
    # type: () -> tuple[str, ...]
    return __all__
