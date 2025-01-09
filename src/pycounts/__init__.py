# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts")

from pycounts.pycounts import (
    count_words,
    load_text,
    clean_text
)
from pycounts.plotting import plot_words

__all__ = [
    "count_words",
    "load_text",
    "clean_text",
    "plot_words"
]