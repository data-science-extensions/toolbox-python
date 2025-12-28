# ============================================================================ #
#                                                                              #
#     Title: Checkers                                                          #
#     Purpose: Check certain values against other objects.                     #
#                                                                              #
# ============================================================================ #


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Overview                                                              ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Description                                                              ####
# ---------------------------------------------------------------------------- #


"""
!!! note "Summary"
    This module provides functions to check certain values against other objects. It includes type checking, value validation, and membership checks.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import operator
from typing import Any, Callable, Union, overload

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import (
    any_collection,
    scalar,
    str_collection,
    str_list,
)


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: str_list = [
    "OPERATORS",
    "is_value_of_type",
    "is_all_values_of_type",
    "is_any_values_of_type",
    "is_value_in_iterable",
    "is_all_values_in_iterable",
    "is_any_values_in_iterable",
    "is_valid_value",
    "is_type",
    "is_all_type",
    "is_any_type",
    "is_in",
    "is_any_in",
    "is_all_in",
    "is_valid",
    "assert_value_of_type",
    "assert_all_values_of_type",
    "assert_any_values_of_type",
    "assert_value_in_iterable",
    "assert_any_values_in_iterable",
    "assert_all_values_in_iterable",
    "assert_is_valid_value",
    "assert_type",
    "assert_is_type",
    "assert_all_type",
    "assert_all_is_type",
    "assert_any_type",
    "assert_any_is_type",
    "assert_in",
    "assert_any_in",
    "assert_all_in",
    "assert_is_valid",
    "any_element_contains",
    "all_elements_contains",
    "get_elements_containing",
]


## --------------------------------------------------------------------------- #
##  Constants                                                               ####
## --------------------------------------------------------------------------- #


OPERATORS: dict[str, Callable[[Any, Any], bool]] = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne,
    "in": lambda a, b: operator.contains(b, a),
    "not in": lambda a, b: not operator.contains(b, a),
    "is": operator.is_,
    "is not": operator.is_not,
}


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Main Section                                                          ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  `is_*()` functions                                                      ####
## --------------------------------------------------------------------------- #


@overload
def is_value_of_type(value: Any, check_type: type) -> bool: ...
@overload
def is_value_of_type(value: Any, check_type: tuple[type, ...]) -> bool: ...
@overload
def is_value_of_type(value: Any, check_type: list[type]) -> bool: ...
def is_value_of_type(value: Any, check_type: Union[type, tuple[type, ...], list[type]]) -> bool:
    """
    !!! note "Summary"
        Check if a given value is of a specified type or types.

    ???+ abstract "Details"
        This function is used to verify if a given value matches a specified type or any of the types in a tuple of types.

    Params:
        value (Any):
            The value to check.
        check_type (Union[type, tuple[type, ...], list[type]]):
            The type or tuple of types to check against.

    Returns:
        (bool):
            `#!py True` if the value is of the specified type or one of the specified types; `#!py False` otherwise.

    ???+ example "Examples"

        Check if a value is of a specific type:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_value_of_type
        >>> value = 42
        >>> check_type = int
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if value is of type `#!py int`"}
        >>> is_value_of_type(value, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: The value is of type `#!py int`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if value is of type `#!py str`"}
        >>> is_value_of_type(value, str)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: The value is not of type `#!py str`."
        </div>

    ??? tip "See Also"
        - [`is_value_of_type()`][toolbox_python.checkers.is_value_of_type]
        - [`is_type()`][toolbox_python.checkers.is_type]
    """
    check_type = tuple(check_type) if isinstance(check_type, list) else check_type
    return isinstance(value, check_type)


@overload
def is_all_values_of_type(values: any_collection, check_type: type) -> bool: ...
@overload
def is_all_values_of_type(values: any_collection, check_type: tuple[type, ...]) -> bool: ...
@overload
def is_all_values_of_type(values: any_collection, check_type: list[type]) -> bool: ...
def is_all_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...], list[type]],
) -> bool:
    """
    !!! note "Summary"
        Check if all values in an iterable are of a specified type or types.

    ???+ abstract "Details"
        This function is used to verify if all values in a given iterable match a specified type or any of the types in a tuple of types.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type, ...], list[type]]):
            The type or tuple of types to check against.

    Returns:
        (bool):
            `#!py True` if all values are of the specified type or one of the specified types; `#!py False` otherwise.

    ???+ example "Examples"

        Check if all values in an iterable are of a specific type:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_all_values_of_type
        >>> values = [1, 2, 3]
        >>> check_type = int
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if all values are of type `#!py int`"}
        >>> is_all_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: All values are of type `#!py int`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if all values are of type `#!py str`"}
        >>> is_all_values_of_type(values, str)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: Not all values are of type `#!py str`."
        </div>

    ??? tip "See Also"
        - [`is_value_of_type()`][toolbox_python.checkers.is_value_of_type]
        - [`is_all_values_of_type()`][toolbox_python.checkers.is_all_values_of_type]
        - [`is_type()`][toolbox_python.checkers.is_type]
        - [`is_all_type()`][toolbox_python.checkers.is_all_type]
    """
    check_type = tuple(check_type) if isinstance(check_type, list) else check_type
    return all(isinstance(value, check_type) for value in values)


@overload
def is_any_values_of_type(values: any_collection, check_type: type) -> bool: ...
@overload
def is_any_values_of_type(values: any_collection, check_type: tuple[type, ...]) -> bool: ...
@overload
def is_any_values_of_type(values: any_collection, check_type: list[type]) -> bool: ...
def is_any_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...], list[type]],
) -> bool:
    """
    !!! note "Summary"
        Check if any value in an iterable is of a specified type or types.

    ???+ abstract "Details"
        This function is used to verify if any value in a given iterable matches a specified type or any of the types in a tuple of types.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type, ...], list[type]]):
            The type or tuple of types to check against.

    Returns:
        (bool):
            `#!py True` if any value is of the specified type or one of the specified types; `#!py False` otherwise.

    ???+ example "Examples"

        Check if any value in an iterable is of a specific type:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_any_values_of_type
        >>> values = [1, "a", 3.0]
        >>> check_type = str
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if any value is of type `#!py str`"}
        >>> is_any_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: At least one value is of type `#!py str`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if any value is of type `#!py dict`"}
        >>> is_any_values_of_type(values, dict)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: No values are of type `#!py dict`."
        </div>

    ??? tip "See Also"
        - [`is_value_of_type()`][toolbox_python.checkers.is_value_of_type]
        - [`is_any_values_of_type()`][toolbox_python.checkers.is_any_values_of_type]
        - [`is_type()`][toolbox_python.checkers.is_type]
        - [`is_any_type()`][toolbox_python.checkers.is_any_type]
    """
    check_type = tuple(check_type) if isinstance(check_type, list) else check_type
    return any(isinstance(value, check_type) for value in values)


@typechecked
def is_value_in_iterable(
    value: scalar,
    iterable: any_collection,
) -> bool:
    """
    !!! note "Summary"
        Check if a given value is present in an iterable.

    ???+ abstract "Details"
        This function is used to verify if a given value exists within an iterable such as a list, tuple, or set.

    Params:
        value (scalar):
            The value to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if the value is found in the iterable; `#!py False` otherwise.

    ???+ example "Examples"

        Check if a value is in an iterable:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_value_in_iterable
        >>> value = 2
        >>> iterable = [1, 2, 3]
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if value is in the iterable"}
        >>> is_value_in_iterable(value, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: The value is in the iterable."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if value is not in the iterable"}
        >>> is_value_in_iterable(4, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: The value is not in the iterable."
        </div>

    ??? tip "See Also"
        - [`is_value_in_iterable()`][toolbox_python.checkers.is_value_in_iterable]
        - [`is_in()`][toolbox_python.checkers.is_in]
    """
    return value in iterable


@typechecked
def is_all_values_in_iterable(
    values: any_collection,
    iterable: any_collection,
) -> bool:
    """
    !!! note "Summary"
        Check if all values in an iterable are present in another iterable.

    ???+ abstract "Details"
        This function is used to verify if all values in a given iterable exist within another iterable.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if all values are found in the iterable; `#!py False` otherwise.

    ???+ example "Examples"

        Check if all values in an iterable are present in another iterable:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_all_values_in_iterable
        >>> values = [1, 2]
        >>> iterable = [1, 2, 3]
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if all values are in the iterable"}
        >>> is_all_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: All values are in the iterable."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if all values are not in the iterable"}
        >>> is_all_values_in_iterable([1, 4], iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: Not all values are in the iterable."
        </div>

    ??? tip "See Also"
        - [`is_value_in_iterable()`][toolbox_python.checkers.is_value_in_iterable]
        - [`is_all_values_of_type()`][toolbox_python.checkers.is_all_values_of_type]
        - [`is_in()`][toolbox_python.checkers.is_in]
        - [`is_all_in()`][toolbox_python.checkers.is_all_in]
    """
    return all(value in iterable for value in values)


@typechecked
def is_any_values_in_iterable(
    values: any_collection,
    iterable: any_collection,
) -> bool:
    """
    !!! note "Summary"
        Check if any value in an iterable is present in another iterable.

    ???+ abstract "Details"
        This function is used to verify if any value in a given iterable exists within another iterable.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if any value is found in the iterable; `#!py False` otherwise.

    ???+ example "Examples"

        Check if any value in an iterable is present in another iterable:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_any_values_in_iterable
        >>> values = [1, 4]
        >>> iterable = [1, 2, 3]
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if any value is in the iterable"}
        >>> is_any_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: At least one value is in the iterable."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if any value is not in the iterable"}
        >>> is_any_values_in_iterable([4, 5], iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: None of the values are in the iterable."
        </div>

    ??? tip "See Also"
        - [`is_value_in_iterable()`][toolbox_python.checkers.is_value_in_iterable]
        - [`is_any_values_of_type()`][toolbox_python.checkers.is_any_values_of_type]
        - [`is_in()`][toolbox_python.checkers.is_in]
        - [`is_any_in()`][toolbox_python.checkers.is_any_in]
    """
    return any(value in iterable for value in values)


def is_valid_value(value: Any, op: str, target: Any) -> bool:
    """
    !!! note "Summary"
        Check if a value is valid based on a specified operator and target.

    ???+ abstract "Details"
        This function checks if a given value meets a condition defined by an operator when compared to a target value. The operator can be one of the predefined operators in the [`OPERATORS`][toolbox_python.checkers.OPERATORS] dictionary.

    Params:
        value (Any):
            The value to check.
        op (str):
            The operator to use for comparison. Valid operators are defined in the [`OPERATORS`][toolbox_python.checkers.OPERATORS] dictionary.
        target (Any):
            The target value to compare against.

    Raises:
        (ValueError):
            If the operator is not recognized or is not valid.

    Returns:
        (bool):
            `#!py True` if the value meets the condition defined by the operator and target; `#!py False` otherwise.

    ???+ example "Examples"

        Check if a value is valid based on an operator and target:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import is_valid_value
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if value is greater than target"}
        >>> is_valid_value(5, ">", 3)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: The value is greater than the target."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if value is less than or equal to target"}
        >>> is_valid_value(5, "<=", 3)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: The value is not less than or equal to the target."
        </div>
    """
    if op not in OPERATORS:
        raise ValueError(f"Unknown operator '{op}'. Valid operators are: {list(OPERATORS.keys())}")
    op_func: Callable[[Any, Any], bool] = OPERATORS[op]
    return op_func(value, target)


### Aliases ----
is_type = is_value_of_type
is_all_type = is_all_values_of_type
is_any_type = is_any_values_of_type
is_in = is_value_in_iterable
is_any_in = is_any_values_in_iterable
is_all_in = is_all_values_in_iterable
is_valid = is_valid_value


## --------------------------------------------------------------------------- #
##  `assert_*()` functions                                                  ####
## --------------------------------------------------------------------------- #


@overload
def assert_value_of_type(value: Any, check_type: type) -> None: ...
@overload
def assert_value_of_type(value: Any, check_type: tuple[type, ...]) -> None: ...
@overload
def assert_value_of_type(value: Any, check_type: list[type]) -> None: ...
def assert_value_of_type(
    value: Any,
    check_type: Union[type, tuple[type, ...], list[type]],
) -> None:
    """
    !!! note "Summary"
        Assert that a given value is of a specified type or types.

    ???+ abstract "Details"
        This function is used to assert that a given value matches a specified type or any of the types in a tuple of types. If the value does not match the specified type(s), a `#!py TypeError` is raised.

    Params:
        value (Any):
            The value to check.
        check_type (Union[type, tuple[type, ...], list[type]]):
            The type or tuple of types to check against.

    Raises:
        (TypeError):
            If the value is not of the specified type or one of the specified types.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the assertion fails.

    ???+ example "Examples"

        Assert that a value is of a specific type:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_value_of_type
        >>> value = 42
        >>> check_type = int
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that value is of type int"}
        >>> assert_value_of_type(value, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is of type `#!py int`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that value is of type str"}
        >>> assert_value_of_type(value, str)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        TypeError: Value '42' is not correct type: 'int'. Must be: 'str'
        ```
        !!! failure "Conclusion: The value is not of type `#!py str`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 3: Assert that value is of type int or float"}
        >>> assert_value_of_type(value, (int, float))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is of type `#!py int` or `#!py float`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 4: Assert that value is of type str or dict"}
        >>> assert_value_of_type(value, (str, dict))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        TypeError: Value '42' is not correct type: 'int'. Must be: 'str' or 'dict'.
        ```
        !!! failure "Conclusion: The value is not of type `#!py str` or `#!py dict`."
        </div>

    ??? tip "See Also"
        - [`is_value_of_type()`][toolbox_python.checkers.is_value_of_type]
        - [`is_type()`][toolbox_python.checkers.is_type]
    """
    if not is_type(value=value, check_type=check_type):
        msg: str = f"Value '{value}' is not correct type: '{type(value).__name__}'. "
        if isinstance(check_type, type):
            msg += f"Must be: '{check_type.__name__}'."
        else:
            msg += f"Must be: '{' or '.join([typ.__name__ for typ in check_type])}'."
        raise TypeError(msg)


@overload
def assert_all_values_of_type(values: any_collection, check_type: type) -> None: ...
@overload
def assert_all_values_of_type(values: any_collection, check_type: tuple[type, ...]) -> None: ...
@overload
def assert_all_values_of_type(values: any_collection, check_type: list[type]) -> None: ...
def assert_all_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...], list[type]],
) -> None:
    """
    !!! note "Summary"
        Assert that all values in an iterable are of a specified type or types.

    ???+ abstract "Details"
        This function is used to assert that all values in a given iterable match a specified type or any of the types in a tuple of types. If any value does not match the specified type(s), a `#!py TypeError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type, ...], list[type]]):
            The type or tuple of types to check against.

    Raises:
        (TypeError):
            If any value is not of the specified type or one of the specified types.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the assertion fails.

    ???+ example "Examples"

        Assert that all values in an iterable are of a specific type:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_all_values_of_type
        >>> values = [1, 2, 3]
        >>> check_type = int
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that all values are of type int"}
        >>> assert_all_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: All values are of type `#!py int`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that all values are of type str"}
        >>> assert_all_values_of_type(values, str)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        TypeError: Some elements [1, 2, 3] have the incorrect type ['int', 'int', 'int']. Must be 'str'
        ```
        !!! failure "Conclusion: Not all values are of type `#!py str`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 3: Assert that all values are of type int or float"}
        >>> assert_all_values_of_type(values, (int, float))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: All values are of type `#!py int` or `#!py float`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 4: Assert that all values are of type str or dict"}
        >>> assert_all_values_of_type(values, (str, dict))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        TypeError: Some elements [1, 2, 3] have the incorrect type ['int', 'int', 'int']. Must be: 'str' or 'dict'
        ```
        !!! failure "Conclusion: Not all values are of type `#!py str` or `#!py dict`."
        </div>

    ??? tip "See Also"
        - [`is_value_of_type()`][toolbox_python.checkers.is_value_of_type]
        - [`is_all_values_of_type()`][toolbox_python.checkers.is_all_values_of_type]
        - [`is_type()`][toolbox_python.checkers.is_type]
        - [`is_all_type()`][toolbox_python.checkers.is_all_type]
    """
    if not is_all_type(values=values, check_type=check_type):
        invalid_values = [value for value in values if not is_type(value, check_type)]
        invalid_types = [f"'{type(value).__name__}'" for value in values if not is_type(value, check_type)]
        msg: str = f"Some elements {invalid_values} have the incorrect type {invalid_types}. "
        if isinstance(check_type, type):
            msg += f"Must be '{check_type}'"
        else:
            types: str_list = [f"'{typ.__name__}'" for typ in check_type]
            msg += f"Must be: {' or '.join(types)}"
        raise TypeError(msg)


@overload
def assert_any_values_of_type(values: any_collection, check_type: type) -> None: ...
@overload
def assert_any_values_of_type(values: any_collection, check_type: tuple[type, ...]) -> None: ...
@overload
def assert_any_values_of_type(values: any_collection, check_type: list[type]) -> None: ...
def assert_any_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...], list[type]],
) -> None:
    """
    !!! note "Summary"
        Assert that any value in an iterable is of a specified type or types.

    ???+ abstract "Details"
        This function is used to assert that at least one value in a given iterable matches a specified type or any of the types in a tuple of types. If none of the values match the specified type(s), a `#!py TypeError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type, ...], list[type]]):
            The type or tuple of types to check against.

    Raises:
        (TypeError):
            If none of the values are of the specified type or one of the specified types.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the assertion fails.

    ???+ example "Examples"

        Assert that any value in an iterable is of a specific type:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_any_values_of_type
        >>> values = [1, "a", 3.0]
        >>> check_type = str
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that any value is of type str"}
        >>> assert_any_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: At least one value is of type `#!py str`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that any value is of type dict"}
        >>> assert_any_values_of_type(values, dict)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        TypeError: None of the elements in [1, 'a', 3.0] have the correct type. Must be: 'dict'
        ```
        !!! failure "Conclusion: None of the values are of type `#!py dict`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 3: Assert that any value is of type int or float"}
        >>> assert_any_values_of_type(values, (int, float))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: At least one value is of type `#!py int` or `#!py float`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 4: Assert that any value is of type dict or list"}
        >>> assert_any_values_of_type(values, (dict, list))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        TypeError: None of the elements in [1, 'a', 3.0] have the correct type. Must be: 'dict' or 'list'
        ```
        !!! failure "Conclusion: None of the values are of type `#!py dict` or `#!py list`."
        </div>

    ??? tip "See Also"
        - [`is_value_of_type()`][toolbox_python.checkers.is_value_of_type]
        - [`is_any_values_of_type()`][toolbox_python.checkers.is_any_values_of_type]
        - [`is_type()`][toolbox_python.checkers.is_type]
        - [`is_any_type()`][toolbox_python.checkers.is_any_type]
    """
    if not is_any_type(values=values, check_type=check_type):
        invalid_values = [value for value in values if not is_type(value, check_type)]
        msg: str = f"None of the elements in {invalid_values} have the correct type. "
        if isinstance(check_type, type):
            msg += f"Must be: '{check_type.__name__}'"
        else:
            types: str_list = [f"'{typ.__name__}'" for typ in check_type]
            msg += f"Must be: {' or '.join(types)}"
        raise TypeError(msg)


def assert_value_in_iterable(
    value: scalar,
    iterable: any_collection,
) -> None:
    """
    !!! note "Summary"
        Assert that a given value is present in an iterable.

    ???+ abstract "Details"
        This function is used to assert that a given value exists within an iterable such as a `#!py list`, `#!py tuple`, or `#!py set`. If the value is not found in the iterable, a `#!py LookupError` is raised.

    Params:
        value (scalar):
            The value to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (LookupError):
            If the value is not found in the iterable.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the assertion fails.

    ???+ example "Examples"

        Assert that a value is in an iterable:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_value_in_iterable
        >>> value = 2
        >>> iterable = [1, 2, 3]
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that value is in the iterable"}
        >>> assert_value_in_iterable(value, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is in the iterable."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that value is not in the iterable"}
        >>> assert_value_in_iterable(4, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        LookupError: Value '4' not found in iterable: [1, 2, 3]
        ```
        !!! failure "Conclusion: The value is not in the iterable."
        </div>

    ??? tip "See Also"
        - [`is_value_in_iterable()`][toolbox_python.checkers.is_value_in_iterable]
        - [`is_in()`][toolbox_python.checkers.is_in]
    """
    if not is_in(value=value, iterable=iterable):
        raise LookupError(f"Value '{value}' not found in iterable: {iterable}")


def assert_any_values_in_iterable(
    values: any_collection,
    iterable: any_collection,
) -> None:
    """
    !!! note "Summary"
        Assert that any value in an iterable is present in another iterable.

    ???+ abstract "Details"
        This function is used to assert that at least one value in a given iterable exists within another iterable. If none of the values are found in the iterable, a `#!py LookupError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (LookupError):
            If none of the values are found in the iterable.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the assertion fails.

    ???+ example "Examples"

        Assert that any value in an iterable is present in another iterable:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_any_values_in_iterable
        >>> values = [1, 4]
        >>> iterable = [1, 2, 3]
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that any value is in the iterable"}
        >>> assert_any_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: At least one value is in the iterable."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that any value is not in the iterable"}
        >>> assert_any_values_in_iterable([4, 5], iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        LookupError: None of the values in [4, 5] can be found in [1, 2, 3]
        ```
        !!! failure "Conclusion: None of the values are in the iterable."
        </div>

    ??? tip "See Also"
        - [`is_value_in_iterable()`][toolbox_python.checkers.is_value_in_iterable]
        - [`is_any_values_of_type()`][toolbox_python.checkers.is_any_values_of_type]
        - [`is_in()`][toolbox_python.checkers.is_in]
        - [`is_any_in()`][toolbox_python.checkers.is_any_in]
    """
    if not is_any_in(values=values, iterable=iterable):
        raise LookupError(f"None of the values in {values} can be found in {iterable}")


def assert_all_values_in_iterable(
    values: any_collection,
    iterable: any_collection,
) -> None:
    """
    !!! note "Summary"
        Assert that all values in an iterable are present in another iterable.

    ???+ abstract "Details"
        This function is used to assert that all values in a given iterable exist within another iterable. If any value is not found in the iterable, a `#!py LookupError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (LookupError):
            If any value is not found in the iterable.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the assertion fails.

    ???+ example "Examples"

        Assert that all values in an iterable are present in another iterable:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_all_values_in_iterable
        >>> values = [1, 2]
        >>> iterable = [1, 2, 3]
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that all values are in the iterable"}
        >>> assert_all_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: All values are in the iterable."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that all values are not in the iterable"}
        >>> assert_all_values_in_iterable([1, 4], iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        LookupError: Some values [4] are missing from [1, 2, 3]
        ```
        !!! failure "Conclusion: Not all values are in the iterable."
        </div>

    ??? tip "See Also"
        - [`is_value_in_iterable()`][toolbox_python.checkers.is_value_in_iterable]
        - [`is_all_values_of_type()`][toolbox_python.checkers.is_all_values_of_type]
        - [`is_in()`][toolbox_python.checkers.is_in]
        - [`is_all_in()`][toolbox_python.checkers.is_all_in]
    """
    if not is_all_in(values=values, iterable=iterable):
        missing_values = [value for value in values if not is_in(value, iterable)]
        raise LookupError(f"Some values {missing_values} are missing from {iterable}")


def assert_is_valid_value(value: Any, op: str, target: Any) -> None:
    """
    !!! note "Summary"
        Assert that a value is valid based on a specified operator and target.

    ???+ abstract "Details"
        This function checks if a given value meets a condition defined by an operator when compared to a target value. The operator can be one of the predefined operators in the [`OPERATORS`][toolbox_python.checkers.OPERATORS] dictionary. If the condition is not met, a `#!py ValueError` is raised.

    Params:
        value (Any):
            The value to check.
        op (str):
            The operator to use for comparison. Valid operators are defined in the [`OPERATORS`][toolbox_python.checkers.OPERATORS] dictionary.
        target (Any):
            The target value to compare against.

    Raises:
        (ValueError):
            If the operator is not recognized or if the value does not meet the condition defined by the operator and target.

    Returns:
        (None):
            This function does not return a value. It raises an exception if the condition is not met.

    ???+ example "Examples"

        Assert that a value is valid based on an operator and target:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import assert_is_valid_value
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Assert that value is greater than target"}
        >>> assert_is_valid_value(5, ">", 3)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is greater than the target."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Assert that value is less than or equal to target"}
        >>> assert_is_valid_value(5, "<=", 3)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ValueError: Validation failed: '5 <= 3' is not True
        ```
        !!! failure "Conclusion: The value is not less than or equal to the target."
        </div>
    """
    if not is_valid_value(value, op, target):
        raise ValueError(f"Validation failed: '{value} {op} {target}' is not True")


### Aliases ----
assert_type = assert_value_of_type
assert_is_type = assert_value_of_type
assert_all_type = assert_all_values_of_type
assert_all_is_type = assert_all_values_of_type
assert_any_type = assert_any_values_of_type
assert_any_is_type = assert_any_values_of_type
assert_in = assert_value_in_iterable
assert_any_in = assert_any_values_in_iterable
assert_all_in = assert_all_values_in_iterable
assert_is_valid = assert_is_valid_value


## --------------------------------------------------------------------------- #
##  `*_contains()` functions                                                ####
## --------------------------------------------------------------------------- #


@typechecked
def any_element_contains(
    iterable: str_collection,
    check: str,
) -> bool:
    """
    !!! note "Summary"
        Check to see if any element in a given iterable contains a given string value.
        !!! warning "Note: This check _is_ case sensitive."

    ???+ abstract "Details"
        This function is helpful for doing a quick check to see if any element in a `#!py list` contains a given `#!py str` value. For example, checking if any column header contains a specific string value.

    Params:
        iterable (str_collection):
            The iterables to check within. Because this function uses an `#!py in` operation to check if `check` string exists in the elements of `iterable`, therefore all elements of `iterable` must be `#!py str` type.
        check (str):
            The string value to check exists in any of the elements in `iterable`.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if at least one element in `iterable` contains `check` string; `#!py False` if no elements contain `check`.

    ???+ example "Examples"

        Check if any element in an iterable contains a specific string:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import any_element_contains
        >>> iterable = ["apple", "banana", "cherry"]
        >>> check = "an"
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if any element contains 'an'"}
        >>> any_element_contains(iterable, check)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: At least one element contains `'an'`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if any element contains 'xy'"}
        >>> any_element_contains(iterable, "xy")
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: No elements contain `'xy'`."
        </div>
    """
    return any(check in elem for elem in iterable)


@typechecked
def all_elements_contains(iterable: str_collection, check: str) -> bool:
    """
    !!! note "Summary"
        Check to see if all elements in a given iterable contains a given string value.
        !!! warning "Note: This check _is_ case sensitive."

    ???+ abstract "Details"
        This function is helpful for doing a quick check to see if all element in a `#!py list` contains a given `#!py str` value. For example, checking if all columns in a DataFrame contains a specific string value.

    Params:
        iterable (str_collection):
            The iterables to check within. Because this function uses an `#!py in` operation to check if `check` string exists in the elements of `iterable`, therefore all elements of `iterable` must be `#!py str` type.
        check (str):
            The string value to check exists in any of the elements in `iterable`.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if all elements in `iterable` contains `check` string; `#!py False` otherwise.

    ???+ example "Examples"

        Check if all elements in an iterable contain a specific string:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import all_elements_contains
        >>> iterable = ["apple", "banana", "peach"]
        >>> check = "a"
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Check if all elements contain 'a'"}
        >>> all_elements_contains(iterable, check)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: All elements contain `'a'`."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Check if all elements contain 'e'"}
        >>> all_elements_contains(iterable, "e")
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        False
        ```
        !!! failure "Conclusion: Not all elements contain `'e'`."
        </div>
    """
    return all(check in elem for elem in iterable)


@typechecked
def get_elements_containing(iterable: str_collection, check: str) -> tuple[str, ...]:
    """
    !!! note "Summary"
        Extract all elements in a given iterable which contains a given string value.
        !!! warning "Note: This check _is_ case sensitive."

    Params:
        iterable (str_collection):
            The iterables to check within. Because this function uses an `#!py in` operation to check if `check` string exists in the elements of `iterable`, therefore all elements of `iterable` must be `#!py str` type.
        check (str):
            The string value to check exists in any of the elements in `iterable`.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (tuple):
            A `#!py tuple` containing all the string elements from `iterable` which contains the `check` string.

    ???+ example "Examples"

        Extract elements in an iterable that contain a specific string:

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.checkers import get_elements_containing
        >>> iterable = ["apple", "banana", "cherry"]
        >>> check = "an"
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Extract elements containing 'an'"}
        >>> get_elements_containing(iterable, check)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ('banana',)
        ```
        !!! success "Conclusion: The element(s) containing `'an'` are extracted."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Extract elements containing 'xy'"}
        >>> get_elements_containing(iterable, "xy")
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ()
        ```
        !!! failure "Conclusion: No elements contain `'xy'`."
        </div>
    """
    return tuple(elem for elem in iterable if check in elem)
