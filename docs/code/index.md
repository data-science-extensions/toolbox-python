# Modules

## Overview

These are the modules used in this package:

| Module                            | Description |
|-----------------------------------|-------------|
| [Classes](./classes.md)           | The `classes` module is designed for functions to be executed _on_ classes; not _within_ classes.<br>For any methods/functions that should be added _to_ classes, you should consider re-designing the original class, or sub-classing it to make further alterations.
| [Bools](./bools.md)               | The `bools` module is used how to manipulate and enhance Python booleans.<br>Primarily, this module is used to store the `strtobool()` function, which used to be found in the `distutils.util` module, until it was deprecated. As mentioned in [PEP632](https://peps.python.org/pep-0632/#migration-advice), we should re-implement this function in our own code. And that's what we've done here.
| [Lists](./lists.md)               | The `lists` module is used how to manipulate and enhance Python lists.<br>Note that functions in this module will only take-in and manipulate existing `#!py list` objects, and also output `#!py list` objects. It will not sub-class the base `#!py list` object, or create new '`#!py list`-like' objects. It will always remain pure python types at it's core.
| [Strings](./strings.md)           | The `strings` module is for manipulating and checking certain string objects.
| [Dictionaries](./dictionaries.md) | The `dictionaries` module is used how to manipulate and enhance Python dictionaries.<br>Note that functions in this module will only take-in and manipulate existing `#!py dict` objects, and also output `#!py dict` objects. It will not sub-class the base `#!py dict` object, or create new '`#!py dict`-like' objects. It will always remain pure python types at it's core.
| [Checkers](./checkers.md)         | Check certain values against other objects.
| [Output](./output.md)             | The `output` module is for streamlining how data is outputted.<br>This includes `#!py print()`'ing to the terminal and `#!py log()`'ing to files.
| [Retry](./retry.md)               | The `retry` module is for enabling automatic retrying of a given function when a specific `Exception` is thrown.
| [Defaults](./defaults.md)         | The `defaults` module is used how to set and control default values for our various Python processes.

## Testing

This package is fully tested against:

1. Unit tests
1. Lint tests
1. MyPy tests
1. Build tests

Tests are run in matrix against:

1. Python Versions:
    1. `3.8`
    1. `3.9`
    1. `3.10`
    1. `3.11`
    1. `3.12`
    1. `3.13`
1. Operatign Systems:
    1. `ubuntu-latest`
    1. `windows-latest`
    1. `macos-latest`

## Coverage

<div style="position:relative; border:none; width:100%; height:100%; display:block; overflow:auto;">
    <iframe src="./coverage/index.html" style="width:100%; height:600px;"></iframe>
</div>
