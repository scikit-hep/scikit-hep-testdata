#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.

import os.path

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

def get_version():
    g = {}
    exec(open(os.path.join("skhep_testdata", "version.py")).read(), g)
    return g["__version__"]

setup(
    author="Ben Krikler",
    author_email='b.krikler@cern.ch',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Example HEP files for testing and demonstrating",
    install_requires=['pyyaml',
                      'importlib_resources>=1.1',
                      'contextlib2; python_version<"3.3"'],
    license="BSD 3-clause",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['ROOT', 'HEP', 'testing'],
    name='scikit-hep-testdata',
    packages=find_packages(exclude=["tests"]),
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'pytest-pep8'],
    url='https://github.com/scikit-hep/scikit-hep-testdata',
    version = get_version(),
    zip_safe=True,
)
