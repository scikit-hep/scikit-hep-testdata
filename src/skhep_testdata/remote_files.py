# -*- coding: utf-8 -*-
import errno
import logging
import os
import sys
import tarfile
import typing
from typing import Any, Dict, Optional

import yaml

if sys.version_info < (3,):
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources

_default_data_dir = os.path.realpath(os.path.dirname(__file__))


class RemoteDatasetList(object):
    _all_files = {}  # type: Dict[str, Dict[str, str]]

    @classmethod
    def get_config_for_file(cls, filename):
        # type: (str) -> Dict[str, str]
        cls.load_remote_configs()
        config = cls._all_files.get(filename, None)

        if not config:
            raise RuntimeError("Unknown remote file: %s" % filename)

        return config.copy()

    @classmethod
    def load_remote_configs(cls, file_to_load=None):
        # type: (Optional[str]) -> None
        if cls._all_files and file_to_load is None:
            return

        if file_to_load is None:
            dataset_yml = resources.files("skhep_testdata").joinpath(
                "remote_datasets.yml"
            )
            with dataset_yml.open() as infile:
                datasets = yaml.load(infile, Loader=yaml.SafeLoader)
        else:
            with open(file_to_load, "r") as infile:
                datasets = yaml.load(infile, Loader=yaml.SafeLoader)

        for dataset, config in datasets.items():
            files = config["files"]
            if isinstance(files, list):
                files = {f: f for f in files}
                config["files"] = files
            config["dataset_name"] = dataset
            for filename in files.keys():
                scoped_name = os.path.join(dataset, filename)
                cls._all_files[scoped_name] = config

    @classmethod
    def is_known(cls, filename):
        # type: (str) -> bool
        cls.load_remote_configs()
        return filename in cls._all_files


def make_all_dirs(path):
    # type: (str) -> None
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def fetch_remote_dataset(dataset_name, files, url, data_dir):
    # type: (str, Dict[str, str], str, str) -> None
    dataset_dir = os.path.join(data_dir, dataset_name)

    writefile = os.path.join(dataset_dir, os.path.basename(url))
    if os.path.exists(writefile):
        return

    make_all_dirs(dataset_dir)
    logging.warning("Downloading {}".format(url))
    if sys.version_info < (3,):
        typing.cast(Any, urlretrieve)(url, writefile)
    else:
        urlretrieve(url, writefile)

    if tarfile.is_tarfile(writefile):
        logging.warning("Extracting {}".format(writefile))
        with tarfile.open(writefile) as tar:
            members = [tar.getmember(f) for f in files.values()]
            tar.extractall(dataset_dir, members)

        for outfile, infile in files.items():
            full_in = os.path.join(dataset_dir, infile)
            full_out = os.path.join(dataset_dir, outfile)
            os.rename(full_in, full_out)

    if not os.path.exists(writefile):
        msg = "Problem obtaining remote dataset : %s"
        raise RuntimeError(msg % dataset_name)


def is_known_remote(filename):
    # type: (str) -> bool
    return RemoteDatasetList.is_known(filename)


def remote_file(filename, data_dir=_default_data_dir, raise_missing=False):
    # type: (str, str, bool) -> str
    config = RemoteDatasetList.get_config_for_file(filename)
    if not config and raise_missing:
        raise RuntimeError("Unknown %s cannot be found" % filename)
        return None

    path = os.path.join(data_dir, filename)
    if not os.path.isfile(path):
        config["data_dir"] = data_dir
        fetch_remote_dataset(**config)  # type: ignore

    if not os.path.isfile(path) and raise_missing:
        raise RuntimeError("%s cannot be found" % filename)

    return path
