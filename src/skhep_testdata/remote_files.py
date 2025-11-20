from __future__ import annotations

import logging
import tarfile
from importlib import resources
from pathlib import Path
from typing import ClassVar
from urllib.request import urlretrieve

import yaml

from . import data


class RemoteDatasetList:
    _all_files: ClassVar[dict[str, dict[str, str]]] = {}

    @classmethod
    def get_config_for_file(cls, filename: str) -> dict[str, str]:
        cls.load_remote_configs()
        config = cls._all_files.get(filename, None)

        if not config:
            msg = f"Unknown remote file: {filename}"
            raise RuntimeError(msg)

        return config.copy()

    @classmethod
    def load_remote_configs(cls, file_to_load: str | None = None) -> None:
        if cls._all_files and file_to_load is None:
            return

        if file_to_load is None:
            dataset_yml = resources.files("skhep_testdata") / "remote_datasets.yml"
            with dataset_yml.open() as infile:
                datasets = yaml.load(infile, Loader=yaml.SafeLoader)
        else:
            with open(file_to_load) as infile:
                datasets = yaml.load(infile, Loader=yaml.SafeLoader)

        for dataset, config in datasets.items():
            files = config["files"]
            if isinstance(files, list):
                files = {f: f for f in files}
                config["files"] = files
            config["dataset_name"] = dataset
            for filename in files:
                scoped_name = str(Path(dataset) / filename)
                cls._all_files[scoped_name] = config

    @classmethod
    def is_known(cls, filename: str) -> bool:
        cls.load_remote_configs()
        return filename in cls._all_files


def make_all_dirs(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def fetch_remote_dataset(
    dataset_name: str, files: dict[str, str], url: str, cache_dir: str
) -> None:
    dataset_dir = Path(cache_dir) / dataset_name

    writefile = dataset_dir / Path(url).name
    if writefile.exists():
        return

    make_all_dirs(str(dataset_dir))
    logging.warning("Downloading %s", url)
    urlretrieve(url, str(writefile))

    if tarfile.is_tarfile(str(writefile)):
        logging.warning("Extracting %s", writefile)
        with tarfile.open(str(writefile)) as tar:
            members = [tar.getmember(f) for f in files.values()]
            tar.extractall(str(dataset_dir), members)

        for outfile, infile in files.items():
            full_in = dataset_dir / infile
            full_out = dataset_dir / outfile
            full_in.rename(full_out)

    if not writefile.exists():
        msg = "Problem obtaining remote dataset : %s"
        raise RuntimeError(msg % dataset_name)


def is_known_remote(filename: str) -> bool:
    return RemoteDatasetList.is_known(filename)


def remote_file(
    filename: str, cache_dir: str | Path | None = None, raise_missing: bool = False
) -> str:
    cache_dir = data.cache_path(cache_dir)
    config = RemoteDatasetList.get_config_for_file(filename)
    if not config and raise_missing:
        msg = f"Unknown {filename} cannot be found"
        raise RuntimeError(msg)

    path = Path(cache_dir) / filename
    if not path.is_file():
        config["cache_dir"] = str(cache_dir)
        fetch_remote_dataset(**config)  # type: ignore[arg-type]

    if not path.is_file() and raise_missing:
        msg = f"{filename} cannot be found"
        raise RuntimeError(msg)

    return str(path)
