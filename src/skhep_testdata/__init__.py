from __future__ import annotations

from .local_files import data_path, download_all, known_files
from .version import version as __version__

__all__ = ("__version__", "data_path", "download_all", "known_files")


def __dir__() -> tuple[str, ...]:  # pragma: no cover
    return __all__
