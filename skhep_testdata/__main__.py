from __future__ import print_function
import argparse
from . import data_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="skhep_testdata")
    parser.add_argument("file_path", help="path to expand", type=str)
    args = parser.parse_args()

    path = data_path(args.file_path)
    print(path)
