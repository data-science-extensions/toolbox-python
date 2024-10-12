# ============================================================================ #
#                                                                              #
#     Title: Checkers                                                          #
#     Purpose: Check certain values against other objects.                     #
#                                                                              #
# ============================================================================ #


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from typing import Any, Union

# ## Local First Party Imports ----
from toolbox_python.collection_types import collection


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: list[str] = [
    "ITERABLE",
    "SCALAR",
    "assert_all_in",
    "assert_all_type",
    "assert_all_values_in_iterable",
    "assert_all_values_of_type",
    "assert_any_in",
    "assert_any_values_in_iterable",
    "assert_in",
    "assert_type",
    "assert_value_in_iterable",
    "assert_value_of_type",
    "is_all_in",
    "is_all_type",
    "is_all_values_in_iterable",
    "is_all_values_of_type",
    "is_any_in",
    "is_any_values_in_iterable",
    "is_in",
    "is_type",
    "is_value_in_iterable",
    "is_value_of_type",
]


## --------------------------------------------------------------------------- #
##  Types                                                                   ####
## --------------------------------------------------------------------------- #


ITERABLE = collection
SCALAR = Union[str, int, float]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Main Section                                                          ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  `is_*()` functions                                                      ####
## --------------------------------------------------------------------------- #


def is_value_of_type(value: Any, check_type: Union[type, tuple[type]]) -> bool:
    return isinstance(value, check_type)


def is_all_values_of_type(
    values: ITERABLE, check_type: Union[type, tuple[type]]
) -> bool:
    return all(isinstance(value, check_type) for value in values)


def is_value_in_iterable(value: SCALAR, iterable: ITERABLE) -> bool:
    return value in iterable


def is_all_values_in_iterable(values: ITERABLE, iterable: ITERABLE) -> bool:
    return all(value in iterable for value in values)


def is_any_values_in_iterable(values: ITERABLE, iterable: ITERABLE) -> bool:
    return any(value in iterable for value in values)


### Aliases ----
is_type = is_value_of_type
is_all_type = is_all_values_of_type
is_in = is_value_in_iterable
is_any_in = is_any_values_in_iterable
is_all_in = is_all_values_in_iterable


## --------------------------------------------------------------------------- #
##  `assert_*()` functions                                                  ####
## --------------------------------------------------------------------------- #


def assert_value_of_type(value: Any, check_type: Union[type, tuple[type]]) -> None:
    if not is_type(value=value, check_type=check_type):
        raise TypeError(
            f"Values '{value}' is not correct type: '{type(value)}'. "
            "Must be: {check_type}"
        )


def assert_all_values_of_type(
    values: ITERABLE, check_type: Union[type, tuple[type]]
) -> None:
    if not is_all_type(values=values, check_type=check_type):
        invalid_values = [value for value in values if not is_type(value, check_type)]
        invalid_types = [
            type(value) for value in values if not is_type(value, check_type)
        ]
        raise TypeError(
            f"Some elements {invalid_values} have the incorrect type '{type(invalid_types)}'. "
            "Must be {check_type}"
        )


def assert_value_in_iterable(value: SCALAR, iterable: ITERABLE) -> None:
    if not is_in(value=value, iterable=iterable):
        raise LookupError(f"Value '{value}' not found in iterable: {iterable}")


def assert_any_values_in_iterable(values: ITERABLE, iterable: ITERABLE) -> None:
    if not is_any_in(values=values, iterable=iterable):
        raise LookupError(f"None of the values in {values} can be found in {iterable}")


def assert_all_values_in_iterable(values: ITERABLE, iterable: ITERABLE) -> None:
    if not is_all_in(values=values, iterable=iterable):
        missing_values = [value for value in values if not is_in(value, iterable)]
        raise LookupError(f"Some values {missing_values} are missing from {iterable}")


### Aliases ----
assert_type = assert_value_of_type
assert_all_type = assert_all_values_of_type
assert_in = assert_value_in_iterable
assert_any_in = assert_any_values_in_iterable
assert_all_in = assert_all_values_in_iterable
