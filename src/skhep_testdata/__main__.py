# -*- coding: utf-8 -*-
"""
This file will be invoked by python when called with th `-m` options:

```
python -m skhep_testdata cms_hep_2012_tutorial/data.root
```
"""
from __future__ import print_function

import argparse

from . import data_path, download_all, known_files


def main():
    # type: () -> None
    parser = argparse.ArgumentParser(
        prog="skhep_testdata",
        description="Expand a testing dataset path to a full path,"
        " downloading things if a remote file is request.",
    )

    parser.add_argument("--all", action="store_true", help="Download all files")
    parser.add_argument("--list", action="store_true", help="List all files")
    parser.add_argument(
        "--dir",
        type=str,
        default=None,
        help="Path to store in (DEFAULT: ~/.local/skhepdata)",
    )
    parser.add_argument("file_path", help="Path to expand", nargs="*")
    args = parser.parse_args()

    if args.list:
        print(*sorted(known_files), sep="\n")

    if args.all:
        download_all(args.dir)

    for p in args.file_path:
        path = data_path(p, args.dir)
        print(path)


if __name__ == "__main__":
    main()
