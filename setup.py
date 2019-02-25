#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license, see LICENSE.

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


setup(
    author="Ben Krikler",
    author_email='b.krikler@cern.ch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Example HEP files for testing and demonstrating",
    install_requires=['pyyaml'],
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
    version='0.1.1',
    zip_safe=True,
)
