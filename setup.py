# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.

from __future__ import print_function

import os

import setuptools.command.sdist
from setuptools import setup

datafile = "src/skhep_testdata/data"
data_ex = {".root", ".lhe", ".gz"}

data_files = {n for n in os.listdir(datafile) if any(n.endswith(ex) for ex in data_ex)}

if data_files:
    with open(os.path.join(datafile, "file_list.txt"), "w") as f:
        for d in sorted(data_files):
            print(d.split("/")[-1], file=f)


class SDist(setuptools.command.sdist.sdist):
    def make_release_tree(self, base_dir, files):
        new_files = [f for f in files if f[len(datafile) + 1 :] not in data_files]

        setuptools.command.sdist.sdist.make_release_tree(self, base_dir, new_files)


opts = {"include_package_data": True}
include_data = bool(os.environ.get("SKHEP_DATA"))
if not include_data:
    opts["exclude_package_data"] = {
        "": ["*{}".format(ex) for ex in data_ex],
    }
    opts["cmdclass"] = {"sdist": SDist}


setup(**opts)
