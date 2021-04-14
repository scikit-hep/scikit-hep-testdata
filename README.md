[![PyPI version](https://img.shields.io/pypi/v/scikit-hep-testdata.svg?longCache=true)](https://pypi.org/project/scikit-hep-testdata/)
[![Github Actions badge](https://github.com/scikit-hep/scikit-hep-testdata/workflows/CI/badge.svg)](https://github.com/scikit-hep/scikit-hep-testdata/actions)
[![Build Status](https://travis-ci.com/scikit-hep/scikit-hep-testdata.svg?branch=master)](https://travis-ci.com/scikit-hep/scikit-hep-testdata)
[![Coverage Status](https://coveralls.io/repos/github/scikit-hep/scikit-hep-testdata/badge.svg?branch=master)](https://coveralls.io/github/scikit-hep/scikit-hep-testdata?branch=master)

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

The files are not stored on PyPI, so if installed from SDist/wheel, the "local"
files will not be present, but will be downloaded from GitHub and cached in the
`~/.local/skhepdata` directory. If you make an editable install from the Git repo,
or if you set `SKHEP_DATA=1` when building/installing from the Git repo, you will
have the data files locally.

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
- [Listed here](src/skhep_testdata/data)

### Known remote files
- [CMS HEP public tutorial from 2012](http://opendata.cern.ch/record/50)

## Acknowledgements
- Many of the files collected directly within this package were collated originally by Jim Pivarski for [uproot](https://github.com/scikit-hep/uproot)

## Running the tests
This package uses `pytest` to run the unit tests. Install with `pip install scikit-hep-testdata[test]` or `pip install -e .[test]` (dev) to get the testing requirements.
then run:

```bash
pytest
```
