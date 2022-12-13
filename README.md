# scikit-hep-testdata

[![Scikit-HEP][sk-badge]](https://scikit-hep.org/)
[![PyPI version](https://img.shields.io/pypi/v/scikit-hep-testdata.svg?longCache=true)](https://pypi.org/project/scikit-hep-testdata/)
[![Conda latest release](https://img.shields.io/conda/vn/conda-forge/scikit-hep-testdata.svg)](https://github.com/conda-forge/scikit-hep-testdata-feedstock)

[![Github Actions badge](https://github.com/scikit-hep/scikit-hep-testdata/workflows/CI/badge.svg)](https://github.com/scikit-hep/scikit-hep-testdata/actions)
[![Coverage Status](https://coveralls.io/repos/github/scikit-hep/scikit-hep-testdata/badge.svg?branch=main)](https://coveralls.io/github/scikit-hep/scikit-hep-testdata?branch=main)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/scikit-hep/scikit-hep-testdata/main.svg)](https://results.pre-commit.ci/latest/github/scikit-hep/scikit-hep-testdata/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[sk-badge]: https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg

A common package to provide example files (*e.g*. ROOT) for testing and developing packages against.
The sample of files is representative of typical files found "in the wild".

In addition to including some root files directly, this package adds some simple helper methods to
get larger files from common open-access data repositories.

## Installing and usage
To install:

```bash
python -m pip install scikit-hep-testdata
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

You can see all "local" files with `skhep_testdata.known_files`, and you can
download all files at once with `skhep_testdata.download_all()`, optionally selecting
the download cache directory.

### Remote vs. Local files
Some files, particularly large ones, for example, are not stored within this
package and instead live on a remote server; we call these "remote files".  To
obtain these use the same `data_path` method as above, however this will
trigger the code to download and configure the remote file.  This might be slow
the first time round but will subsequently be as fast as for a local file.
WARNING: the local file caching system has not yet been applied to remote
files.

### Command-line invocation
You can also interact with this package from the command-line:

```bash
# Print a path (download if needed)
python -m skhep_testdata cms_hep_2012_tutorial/data.root

# Show all "local" files
python -m skhep_testdata --list

# Download all files to an existing directory
python -m skhep_testdata --all --dir local
```

You can also use `pipx run scikit-hep-testdata` to access the above CLI without installing.


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

## Contributors

We hereby acknowledge the contributors that made this project possible ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="http://benkrikler.github.io"><img src="https://avatars.githubusercontent.com/u/4083697?v=4?s=100" width="100px;" alt="benkrikler"/><br /><sub><b>benkrikler</b></sub></a><br /><a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=benkrikler" title="Code">💻</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=benkrikler" title="Documentation">📖</a></td>
      <td align="center"><a href="https://github.com/jpivarski"><img src="https://avatars.githubusercontent.com/u/1852447?v=4?s=100" width="100px;" alt="Jim Pivarski"/><br /><sub><b>Jim Pivarski</b></sub></a><br /><a href="#maintenance-jpivarski" title="Maintenance">🚧</a> <a href="#data-jpivarski" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=jpivarski" title="Documentation">📖</a></td>
      <td align="center"><a href="http://iscinumpy.dev"><img src="https://avatars.githubusercontent.com/u/4616906?v=4?s=100" width="100px;" alt="Henry Schreiner"/><br /><sub><b>Henry Schreiner</b></sub></a><br /><a href="#maintenance-henryiii" title="Maintenance">🚧</a> <a href="#data-henryiii" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=henryiii" title="Code">💻</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=henryiii" title="Documentation">📖</a></td>
      <td align="center"><a href="http://cern.ch/eduardo.rodrigues"><img src="https://avatars.githubusercontent.com/u/5013581?v=4?s=100" width="100px;" alt="Eduardo Rodrigues"/><br /><sub><b>Eduardo Rodrigues</b></sub></a><br /><a href="#maintenance-eduardo-rodrigues" title="Maintenance">🚧</a> <a href="#data-eduardo-rodrigues" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=eduardo-rodrigues" title="Code">💻</a></td>
      <td align="center"><a href="http://www.matthewfeickert.com/"><img src="https://avatars.githubusercontent.com/u/5142394?v=4?s=100" width="100px;" alt="Matthew Feickert"/><br /><sub><b>Matthew Feickert</b></sub></a><br /><a href="#data-matthewfeickert" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=matthewfeickert" title="Code">💻</a></td>
      <td align="center"><a href="https://cs.purdue.edu/homes/das160"><img src="https://avatars.githubusercontent.com/u/11775615?v=4?s=100" width="100px;" alt="Pratyush Das"/><br /><sub><b>Pratyush Das</b></sub></a><br /><a href="#data-reikdas" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=reikdas" title="Code">💻</a></td>
      <td align="center"><a href="http://blog.jling.dev"><img src="https://avatars.githubusercontent.com/u/5306213?v=4?s=100" width="100px;" alt="Jerry Ling"/><br /><sub><b>Jerry Ling</b></sub></a><br /><a href="#data-Moelf" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=Moelf" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/jonas-eschle"><img src="https://avatars.githubusercontent.com/u/17454848?v=4?s=100" width="100px;" alt="Jonas Eschle"/><br /><sub><b>Jonas Eschle</b></sub></a><br /><a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=jonas-eschle" title="Code">💻</a></td>
      <td align="center"><a href="https://giordonstark.com/"><img src="https://avatars.githubusercontent.com/u/761483?v=4?s=100" width="100px;" alt="Giordon Stark"/><br /><sub><b>Giordon Stark</b></sub></a><br /><a href="#data-kratsg" title="Data">🔣</a> <a href="https://github.com/scikit-hep/scikit-hep-testdata/commits?author=kratsg" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/veprbl"><img src="https://avatars.githubusercontent.com/u/245573?v=4?s=100" width="100px;" alt="Dmitry Kalinkin"/><br /><sub><b>Dmitry Kalinkin</b></sub></a><br /><a href="#data-veprbl" title="Data">🔣</a></td>
      <td align="center"><a href="https://www.df.unito.it/do/docenti.pl/Show?_id=mperesan#tab-profilo"><img src="https://avatars.githubusercontent.com/u/17836610?v=4?s=100" width="100px;" alt="Michele Peresano"/><br /><sub><b>Michele Peresano</b></sub></a><br /><a href="#data-HealthyPear" title="Data">🔣</a></td>
      <td align="center"><a href="https://github.com/lobis"><img src="https://avatars.githubusercontent.com/u/35803280?v=4?s=100" width="100px;" alt="Luis Antonio Obis Aparicio"/><br /><sub><b>Luis Antonio Obis Aparicio</b></sub></a><br /><a href="#data-lobis" title="Data">🔣</a></td>
      <td align="center"><a href="https://github.com/oshadura"><img src="https://avatars.githubusercontent.com/u/7012420?v=4?s=100" width="100px;" alt="Oksana Shadura"/><br /><sub><b>Oksana Shadura</b></sub></a><br /><a href="#data-oshadura" title="Data">🔣</a></td>
      <td align="center"><a href="https://github.com/nsmith-"><img src="https://avatars.githubusercontent.com/u/6587412?v=4?s=100" width="100px;" alt="Nicholas Smith"/><br /><sub><b>Nicholas Smith</b></sub></a><br /><a href="#data-nsmith-" title="Data">🔣</a></td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/beojan"><img src="https://avatars.githubusercontent.com/u/3727925?v=4?s=100" width="100px;" alt="Beojan Stanislaus"/><br /><sub><b>Beojan Stanislaus</b></sub></a><br /><a href="#data-beojan" title="Data">🔣</a></td>
      <td align="center"><a href="http://www.lukasheinrich.com"><img src="https://avatars.githubusercontent.com/u/2318083?v=4?s=100" width="100px;" alt="Lukas"/><br /><sub><b>Lukas</b></sub></a><br /><a href="#data-lukasheinrich" title="Data">🔣</a></td>
      <td align="center"><a href="https://github.com/8me"><img src="https://avatars.githubusercontent.com/u/17862090?v=4?s=100" width="100px;" alt="Johannes Schumann"/><br /><sub><b>Johannes Schumann</b></sub></a><br /><a href="#data-8me" title="Data">🔣</a></td>
      <td align="center"><a href="https://github.com/ekauffma"><img src="https://avatars.githubusercontent.com/u/65742271?v=4?s=100" width="100px;" alt="Elliott Kauffman"/><br /><sub><b>Elliott Kauffman</b></sub></a><br /><a href="#data-ekauffma" title="Data">🔣</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.

## Acknowledgements
- Many of the files collected directly within this package were collated originally by Jim Pivarski for [uproot](https://github.com/scikit-hep/uproot)

## Running the tests
This package uses `pytest` to run the unit tests. Install with `pip install scikit-hep-testdata[test]` or `pip install -e .[test]` (dev) to get the testing requirements.
then run:

```bash
pytest
```
