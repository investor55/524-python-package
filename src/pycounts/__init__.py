# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts-524-J-Test")

from pycounts_524_J_Test.pycounts import (
    count_words,
    load_text,
    clean_text
)
from pycounts_524_J_Test.plotting import plot_words

__all__ = [
    "count_words",
    "load_text",
    "clean_text",
    "plot_words"
]