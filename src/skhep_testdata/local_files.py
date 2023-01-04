from __future__ import annotations

import sys
import tempfile
import zipfile
from pathlib import Path

import requests

from . import data, remote_files

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources

__all__ = ("data_path", "download_all", "known_files")


DIR = Path(__file__).parent.resolve()

baseurl = "https://raw.githubusercontent.com/scikit-hep/scikit-hep-testdata/main/src/skhep_testdata/data/"
zipurl = "https://github.com/scikit-hep/scikit-hep-testdata/zipball/main"


with resources.as_file(resources.files(data) / "file_list.txt") as fp, fp.open() as f:
    known_files = {n.strip() for n in f if n.strip()}


def _cache_path(cache_dir: str | None = None) -> Path:
    if cache_dir is None:
        skhepdir = Path.home() / ".local" / "skhepdata"
        skhepdir.mkdir(exist_ok=True, parents=True)
        return skhepdir
    else:
        return Path(cache_dir)


def data_path(
    filename: str, raise_missing: bool = True, cache_dir: str | None = None
) -> str:
    if remote_files.is_known_remote(filename):
        return remote_files.remote_file(filename, raise_missing=raise_missing)

    if filename not in known_files and raise_missing:
        raise FileNotFoundError(filename)

    filepath = DIR / "data" / filename

    if not filepath.exists() and filename in known_files:
        cached_path = _cache_path(cache_dir) / filename

        if not cached_path.exists():
            # Currently get from main branch
            # Could locally cache if not fixable, or always cache locally
            # Could verify exists first
            # Download all not implemented
            response = requests.get(baseurl + filename)
            response.raise_for_status()
            with cached_path.open("wb") as f:
                f.write(response.content)
        return str(cached_path)

    return str(filepath)


def download_all(cache_dir: str | None = None) -> None:
    local_dir = _cache_path(cache_dir)

    with tempfile.TemporaryFile() as f:
        with requests.get(zipurl, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        with zipfile.ZipFile(f) as z:
            for n in z.namelist():
                if "src/skhep_testdata/data/" in n and not n.endswith(".py"):
                    z.extract(n, str(local_dir / str(n.split("/")[-1])))
