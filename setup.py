#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    description="Example ROOT files for testing and demonstrating",
    install_requires=[],
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords=['ROOT', 'HEP'],
    name='scikit-example-root-files',
    packages=find_packages(),
    test_suite='tests',
    tests_require=['pytest', 'uproot'],
    url='https://github.com/benkrikler/scikit-example-root-files',
    version='0.1.0',
    zip_safe=True,
)
