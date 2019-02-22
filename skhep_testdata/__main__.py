"""
This file will be invoked by python when called with th `-m` options:

```
python -m skhep_testdata cms_hep_2012_tutorial/data.root
```
"""
from __future__ import print_function
import argparse
from . import data_path


if __name__ == "__main__":
    description = "Expand a testing dataset path to a full path,"
    description += " downloading things if a remote file is request."
    parser = argparse.ArgumentParser(prog="skhep_testdata")
    parser.add_argument("file_path", help="path to expand", type=str)
    args = parser.parse_args()

    path = data_path(args.file_path)
    print(path)
