"""
Python Toolbox

A collection of utility functions and classes for Python development.
"""

# ## Python StdLib Imports ----
from importlib.metadata import metadata


### Define package metadata ----
_metadata = metadata("toolbox-python")
__name__: str = _metadata["Name"]
__version__: str = _metadata["Version"]
__author__: str = _metadata["Author"]
__author_email__: str = _metadata["Author-email"]
