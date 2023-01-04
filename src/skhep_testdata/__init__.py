from __future__ import annotations

from .local_files import data_path, download_all, known_files
from .version import version as __version__

__all__ = ("data_path", "download_all", "known_files", "__version__")


def __dir__() -> tuple[str, ...]:
    return __all__
