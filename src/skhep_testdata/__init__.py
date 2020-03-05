from __future__ import absolute_import

from .local_files import data_path

# Convenient access to the version number
from .version import version as __version__

__all__ = ["data_path"]
