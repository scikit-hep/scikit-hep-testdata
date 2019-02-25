[![PyPI version](https://img.shields.io/pypi/v/scikit-hep-testdata.svg?longCache=true)](https://pypi.org/project/scikit-hep-testdata/)
[![Build Status](https://travis-ci.com/scikit-hep/scikit-hep-testdata.svg?branch=master)](https://travis-ci.com/scikit-hep/scikit-hep-testdata)
[![codecov](https://img.shields.io/codecov/c/github/scikit-hep/scikit-hep-testdata/master.svg?longCache=true)](https://codecov.io/gh/scikit-hep/scikit-hep-testdata)

scikit-hep-testdata
===================

A common package to provide example files (*e.g*. ROOT) for testing and developing packages against.
The sample of files is representative of typical files found "in the wild".

In addition to including some root files directly, this package adds some simple helper methods to
get larger files from common open-access data repositories.

## Installing and usage
To install:
```bash
pip install scikit-hep-testdata
```

Once installed, absolute file paths can be resolved using the helper methods:
``` python
from skhep_testdata import data_path

filename = data_path("some_file.root")
```
By default, if an unknown file is requested an exception is raised but this can be skipped by passing the above method `raise_missing=False`:
```python
filename = data_path("unknown_file.root", raise_missing=False)
```

### Remote vs. Local files
Some files, particularly large ones, for example, are not stored within this package and instead live on a remote server; we call these "remote files".
To obtain these use the same `data_path` method as above, however this will trigger the code to download and configure the remote file. 
This might be slow the first time round but will subsequently be as fast as for a local file.

### Command-line invocation
You can also interact with this package from the command-line:
```bash
python -m skhep_testdata cms_hep_2012_tutorial/data.root
```

## Adding new files
We're on the look out for new, interesting files!
- *Large files*: If the file is particularly large, for example > 25 MB, it might be worth adding to an external open access data repository and adding a configuration here so that the internal helper methods can pull this down.
- *Experiment data policies*: Please make sure you have permissions to add the file to this collection, and that any private or sensitive data has been appropriately masked, salted, or scrambled.

## List of files
The following lists describe the files known by this package.

### Files stored in this package
-

### Known remote files
- [CMS HEP public tutorial from 2012](http://opendata.cern.ch/record/50)

## Acknowledgements
- Many of the files collected directly within this package were collated originally by Jim Pivarski for [uproot](https://github.com/scikit-hep/uproot)

## Running the tests
This package uses `pytest` to run the unit tests.
```bash
pytest -vv tests/
```

Use the pytest-cov plugin to get a report on the test coverage:

```bash
pytest --cov=skhep_testdata --cov-report=html -vv tests/
```
