from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import BinaryIO


def cache_path(cache_dir: Path | str | None = None) -> Path:
    if cache_dir is None:
        skhepdir = Path.home() / ".local" / "skhepdata"
        skhepdir.mkdir(exist_ok=True, parents=True)
        return skhepdir

    return Path(cache_dir)


@contextmanager
def atomic_write(path: Path) -> Iterator[BinaryIO]:
    """
    Write to ``path`` via a temporary file, so an interrupted write never
    leaves a partial file that would later be mistaken for a cached one.
    """
    tmp = path.with_name(path.name + ".part")
    try:
        with tmp.open("wb") as f:
            yield f
        tmp.replace(path)
    finally:
        tmp.unlink(missing_ok=True)
