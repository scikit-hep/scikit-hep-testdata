import os
import sys
import tarfile
import errno
import logging


if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve


_default_data_dir = "~/.local/share/scikit_example_root_files/"
_default_data_dir = os.path.expanduser(_default_data_dir)
_remote_dataset_cfg = os.path.realpath(os.path.dirname(__file__))
_remote_dataset_cfg = os.path.join(_remote_dataset_cfg, "remote_datasets.yml")


class RemoteDatasetList(object):
    _all_files = {}

    @classmethod
    def get_config_for_file(cls, filename):
        if not cls._all_files:
            cls.load_remote_configs()

        config = cls._all_files.get(filename, None)

        if not config:
            raise RuntimeError("Unknown remote file: %s" % filename)

        return config.copy()

    @classmethod
    def load_remote_configs(cls):
        import yaml
        with open(_remote_dataset_cfg, "r") as infile:
            datasets = yaml.load(infile)
        for dataset, config in datasets.items():
            files = config["files"]
            if isinstance(files, list):
                files = {f: f for f in files}
                config["files"] = files
            config["dataset_name"] = dataset
            for filename in files.keys():
                scoped_name = os.path.join(dataset, filename)
                cls._all_files[scoped_name] = config
        print("BEK", cls._all_files)


def make_all_dirs(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def fetch_remote_dataset(dataset_name, files, url, data_dir=None):
    if not data_dir:
        data_dir = _default_data_dir
    dataset_dir = os.path.join(data_dir, dataset_name)

    make_all_dirs(dataset_dir)
    writefile = os.path.join(dataset_dir, os.path.basename(url))
    if not os.path.exists(writefile):
        logging.warning("Downloading {}".format(url))
        filename, info = urlretrieve(url, writefile)

    if tarfile.is_tarfile(writefile):
        logging.warning("Extracting {}".format(writefile))
        with tarfile.open(writefile) as tar:
            members = [tar.getmember(f) for f in files.values()]
            tar.extractall(dataset_dir, members)

    for outfile, infile in files.items():
        full_in = os.path.join(dataset_dir, infile)
        full_out = os.path.join(dataset_dir, outfile)
        os.rename(full_in, full_out)

    if not os.path.exists(dataset_dir):
        msg = "Problem obtaining remote dataset : %s"
        raise RuntimeError(msg % dataset_name)

    return data_dir


def remote_file(filename, data_dir=None, raise_missing=False):
    config = RemoteDatasetList.get_config_for_file(filename)
    config["data_dir"] = data_dir
    dataset_dir = fetch_remote_dataset(**config)

    path = os.path.join(dataset_dir, filename)
    if not os.path.isfile(path) and raise_missing:
        raise RuntimeError("%s cannot be found" % filename)

    return path


if __name__ == "__main__":
    print("BEK", remote_file("cms_hep_2012_tutorial/qcd.root"))
