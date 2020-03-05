import os
import sys
import tarfile
import errno
import logging
import importlib_resources
import yaml


if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

_default_data_dir = os.path.realpath(os.path.dirname(__file__))


class RemoteDatasetList(object):
    _all_files = {}

    @classmethod
    def get_config_for_file(cls, filename):
        cls.load_remote_configs()
        config = cls._all_files.get(filename, None)

        if not config:
            raise RuntimeError("Unknown remote file: %s" % filename)

        return config.copy()

    @classmethod
    def load_remote_configs(cls, file_to_load=None):
        if cls._all_files and file_to_load is None:
            return

        if file_to_load is None:
            dataset_yml = importlib_resources.files("skhep_testdata") / "remote_datasets.yml"
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
        cls.load_remote_configs()
        return filename in cls._all_files


def make_all_dirs(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def fetch_remote_dataset(dataset_name, files, url, data_dir):
    dataset_dir = os.path.join(data_dir, dataset_name)

    writefile = os.path.join(dataset_dir, os.path.basename(url))
    if os.path.exists(writefile):
        return

    make_all_dirs(dataset_dir)
    logging.warning("Downloading {}".format(url))
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
    return RemoteDatasetList.is_known(filename)


def remote_file(filename, data_dir=_default_data_dir, raise_missing=False):
    config = RemoteDatasetList.get_config_for_file(filename)
    if not config and raise_missing:
        raise RuntimeError("Unknown %s cannot be found" % filename)
        return None

    path = os.path.join(data_dir, filename)
    if not os.path.isfile(path):
        config["data_dir"] = data_dir
        fetch_remote_dataset(**config)

    if not os.path.isfile(path) and raise_missing:
        raise RuntimeError("%s cannot be found" % filename)

    return path
