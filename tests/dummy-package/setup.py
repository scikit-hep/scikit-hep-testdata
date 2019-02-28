#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    author="scikit-hep-testdata team",
    author_email='b.krikler@cern.ch',
    classifiers=[
        'Development Status :: 3 - Alpha',
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
    description="Dummy package to test scikit-hep-testdata",
    install_requires=['pyyaml', 'scikit-hep-testdata'],
    license="Apache Software License 2.0",
    long_description="This isn't a real package",
    long_description_content_type="text/markdown",
    keywords=['ROOT', 'analysis', 'particle physics', 'HEP', 'F.A.S.T'],
    name='dummy-package',
    packages=find_packages(include=['dummy_package']),
    setup_requires=['pytest-runner'],
    test_suite='tests',
    tests_require=['pytest'],
    url='https://github.com/scikit-hep/scikit-hep-testdata/',
    version='0.1.0'
)
