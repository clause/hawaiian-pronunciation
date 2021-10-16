# Hawaiian Pronunciation

Solution to Kendall Bingham's [Hawaiian Words](http://nifty.stanford.edu/2019/bingham-hawaiian-phonetic-generator/) assignment from [Nifty Assignments](http://nifty.stanford.edu/)

## Prerequistes

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and read through its [User Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html).

## Installation

```shell
conda env create --name hawaiian-pronunciation --file conda.yaml
conda activate hawaiian-pronunciation
```

## Test

```shell
pytest
```
## Project Structure

```
.
├── LICENSE
├── README.md
├── conda.yaml
├── docs
│   └── Hawaiian\ Word\ Phonetic\ Generator.pdf
├── hawaiian.py
└── test_hawaiian.py
```

- `hawaiian.py` contains the entire application.
- `test_hawaiian.py` contains the entire test suite.
- `docs/Hawaiian\ Word\ Phonetic\ Generator.pdf` is a copy of the Hawaiian Word assignment.