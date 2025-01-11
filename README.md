# pycounts-524-J-Test

524 Project

## Installation

```bash
$ pip install pycounts-524-J-Test
```
```bash
$ pip install -i https://test.pypi.org/simple/ pycounts-524-J-Test==0.1.0
```
## Usage

```python
from pycounts_524_J_Test.pycounts import count_words
from pycounts_524_J_Test.plotting import plot_words

# Count words in a text file
word_counts = count_words("path/to/text/file.txt")

# Create a plot of word counts
plot_words(word_counts)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts` was created by Jiayi Li. It is licensed under the terms of the MIT license.

## Credits

`pycounts` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
