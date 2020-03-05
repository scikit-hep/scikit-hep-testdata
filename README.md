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
- `uproot-Event.root`
- `uproot-HZZ-lz4.root`
- `uproot-HZZ-lzma.root`
- `uproot-HZZ-objects.root`
- `uproot-HZZ-uncompressed.root`
- `uproot-HZZ-zlib.root`
- `uproot-HZZ.root`
- `uproot-Zmumu-lz4.root`
- `uproot-Zmumu-lzma.root`
- `uproot-Zmumu-uncompressed.root`
- `uproot-Zmumu-zlib.root`
- `uproot-Zmumu.root`
- `uproot-demo-double32.root`
- `uproot-foriter.root`
- `uproot-foriter2.root`
- `uproot-from-geant4.root`
- `uproot-hepdata-example.root`
- `uproot-histograms.root`
- `uproot-issue124.root`
- `uproot-issue126a.root`
- `uproot-issue126b.root`
- `uproot-issue187.root`
- `uproot-issue21.root`
- `uproot-issue213.root`
- `uproot-issue232.root`
- `uproot-issue30.root`
- `uproot-issue31.root`
- `uproot-issue33.root`
- `uproot-issue38a.root`
- `uproot-issue38b.root`
- `uproot-issue46.root`
- `uproot-issue49.root`
- `uproot-issue57.root`
- `uproot-issue60.root`
- `uproot-issue63.root`
- `uproot-issue64.root`
- `uproot-issue66.root`
- `uproot-issue70.root`
- `uproot-issue74.root`
- `uproot-issue76.root`
- `uproot-issue79.root`
- `uproot-issue96.root`
- `uproot-leaflist.root`
- `uproot-mc10events.root`
- `uproot-nesteddirs.root`
- `uproot-sample-5.23.02-uncompressed.root`
- `uproot-sample-5.23.02-zlib.root`
- `uproot-sample-5.24.00-uncompressed.root`
- `uproot-sample-5.24.00-zlib.root`
- `uproot-sample-5.25.02-uncompressed.root`
- `uproot-sample-5.25.02-zlib.root`
- `uproot-sample-5.26.00-uncompressed.root`
- `uproot-sample-5.26.00-zlib.root`
- `uproot-sample-5.27.02-uncompressed.root`
- `uproot-sample-5.27.02-zlib.root`
- `uproot-sample-5.28.00-uncompressed.root`
- `uproot-sample-5.28.00-zlib.root`
- `uproot-sample-5.29.02-uncompressed.root`
- `uproot-sample-5.29.02-zlib.root`
- `uproot-sample-5.30.00-lzma.root`
- `uproot-sample-5.30.00-uncompressed.root`
- `uproot-sample-5.30.00-zlib.root`
- `uproot-sample-6.08.04-lzma.root`
- `uproot-sample-6.08.04-uncompressed.root`
- `uproot-sample-6.08.04-zlib.root`
- `uproot-sample-6.10.05-lz4.root`
- `uproot-sample-6.10.05-lzma.root`
- `uproot-sample-6.10.05-uncompressed.root`
- `uproot-sample-6.10.05-zlib.root`
- `uproot-sample-6.14.00-lz4.root`
- `uproot-sample-6.14.00-lzma.root`
- `uproot-sample-6.14.00-uncompressed.root`
- `uproot-sample-6.14.00-zlib.root`
- `uproot-simple.root`
- `uproot-small-dy-nooffsets.root`
- `uproot-small-dy-withoffsets.root`
- `uproot-small-evnt-tree-fullsplit.root`
- `uproot-small-evnt-tree-nosplit.root`
- `uproot-small-flat-tree.root`
- `uproot-vectorVectorDouble.root`


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

The pytest-cov plugin is used to get a report on the test coverage:

```bash
pytest --cov=skhep_testdata --cov-report=html -vv tests/
```
