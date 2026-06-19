from __future__ import annotations

from pathlib import Path


def cache_path(cache_dir: Path | str | None = None) -> Path:
    if cache_dir is None:
        skhepdir = Path.home() / ".local" / "skhepdata"
        skhepdir.mkdir(exist_ok=True, parents=True)
        return skhepdir

    return Path(cache_dir)
