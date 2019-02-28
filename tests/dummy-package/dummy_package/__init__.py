from __future__ import print_function
import os
from skhep_testdata import data_path


def run():
    filename = data_path("uproot-Event.root")
    return filename


def debug():
    import skhep_testdata.remote_files as remote
    print("_remote_dataset_cfg", remote._remote_dataset_cfg)

    for root, dirs, files in os.walk(remote._default_data_dir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

if __name__ == "__main__":
    debug()
