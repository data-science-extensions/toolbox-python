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

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import any_collection, scalar, str_collection


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: list[str] = [
    "all_elements_contains",
    "any_element_contains",
    "assert_all_in",
    "assert_all_type",
    "assert_all_values_in_iterable",
    "assert_all_values_of_type",
    "assert_any_in",
    "assert_any_type",
    "assert_any_values_in_iterable",
    "assert_in",
    "assert_type",
    "assert_value_in_iterable",
    "assert_value_of_type",
    "get_elements_containing",
    "is_all_in",
    "is_all_type",
    "is_all_values_in_iterable",
    "is_all_values_of_type",
    "is_any_in",
    "is_any_type",
    "is_any_values_in_iterable",
    "is_in",
    "is_type",
    "is_value_in_iterable",
    "is_value_of_type",
]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Main Section                                                          ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  `is_*()` functions                                                      ####
## --------------------------------------------------------------------------- #


def is_value_of_type(
    value: Any,
    check_type: Union[type, tuple[type, ...]],
) -> bool:
    """
    !!! summary "Summary"
        Check if a given value is of a specified type or types.

    ???+ info "Details"
        This function is used to verify if a given value matches a specified type or any of the types in a tuple of types.

    Params:
        value (Any):
            The value to check.
        check_type (Union[type, tuple[type]]):
            The type or tuple of types to check against.

    Returns:
        (bool):
            `#!py True` if the value is of the specified type or one of the specified types; `#!py False` otherwise.

    ???+ example "Examples"

        Check if a value is of a specific type:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> value = 42
        >>> check_type = int
        ```

        ```{.py .python linenums="1" title="Example 1: Check if value is of type `#!py int`"}
        >>> is_value_of_type(value, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: The value is of type `#!py int`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if value is of type `#!py str`"}
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
    return isinstance(value, check_type)


def is_all_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...]],
) -> bool:
    """
    !!! summary "Summary"
        Check if all values in an iterable are of a specified type or types.

    ???+ info "Details"
        This function is used to verify if all values in a given iterable match a specified type or any of the types in a tuple of types.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type]]):
            The type or tuple of types to check against.

    Returns:
        (bool):
            `#!py True` if all values are of the specified type or one of the specified types; `#!py False` otherwise.

    ???+ example "Examples"

        Check if all values in an iterable are of a specific type:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 2, 3]
        >>> check_type = int
        ```

        ```{.py .python linenums="1" title="Example 1: Check if all values are of type `#!py int`"}
        >>> is_all_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: All values are of type `#!py int`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if all values are of type `#!py str`"}
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
    return all(isinstance(value, check_type) for value in values)


def is_any_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...]],
) -> bool:
    """
    !!! summary "Summary"
        Check if any value in an iterable is of a specified type or types.

    ???+ info "Details"
        This function is used to verify if any value in a given iterable matches a specified type or any of the types in a tuple of types.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type]]):
            The type or tuple of types to check against.

    Returns:
        (bool):
            `#!py True` if any value is of the specified type or one of the specified types; `#!py False` otherwise.

    ???+ example "Examples"

        Check if any value in an iterable is of a specific type:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 'a', 3.0]
        >>> check_type = str
        ```

        ```{.py .python linenums="1" title="Example 1: Check if any value is of type `#!py str`"}
        >>> is_any_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: At least one value is of type `#!py str`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if any value is of type `#!py dict`"}
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
    return any(isinstance(value, check_type) for value in values)


def is_value_in_iterable(
    value: scalar,
    iterable: any_collection,
) -> bool:
    """
    !!! summary "Summary"
        Check if a given value is present in an iterable.

    ???+ info "Details"
        This function is used to verify if a given value exists within an iterable such as a list, tuple, or set.

    Params:
        value (scalar):
            The value to check.
        iterable (any_collection):
            The iterable to check within.

    Returns:
        (bool):
            `#!py True` if the value is found in the iterable; `#!py False` otherwise.

    ???+ example "Examples"

        Check if a value is in an iterable:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> value = 2
        >>> iterable = [1, 2, 3]
        ```

        ```{.py .python linenums="1" title="Example 1: Check if value is in the iterable"}
        >>> is_value_in_iterable(value, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: The value is in the iterable."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if value is not in the iterable"}
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


def is_all_values_in_iterable(
    values: any_collection,
    iterable: any_collection,
) -> bool:
    """
    !!! summary "Summary"
        Check if all values in an iterable are present in another iterable.

    ???+ info "Details"
        This function is used to verify if all values in a given iterable exist within another iterable.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Returns:
        (bool):
            `#!py True` if all values are found in the iterable; `#!py False` otherwise.

    ???+ example "Examples"

        Check if all values in an iterable are present in another iterable:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 2]
        >>> iterable = [1, 2, 3]
        ```

        ```{.py .python linenums="1" title="Example 1: Check if all values are in the iterable"}
        >>> is_all_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: All values are in the iterable."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if all values are not in the iterable"}
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


def is_any_values_in_iterable(
    values: any_collection,
    iterable: any_collection,
) -> bool:
    """
    !!! summary "Summary"
        Check if any value in an iterable is present in another iterable.

    ???+ info "Details"
        This function is used to verify if any value in a given iterable exists within another iterable.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Returns:
        (bool):
            `#!py True` if any value is found in the iterable; `#!py False` otherwise.

    ???+ example "Examples"

        Check if any value in an iterable is present in another iterable:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 4]
        >>> iterable = [1, 2, 3]
        ```

        ```{.py .python linenums="1" title="Example 1: Check if any value is in the iterable"}
        >>> is_any_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: At least one value is in the iterable."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if any value is not in the iterable"}
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


### Aliases ----
is_type = is_value_of_type
is_all_type = is_all_values_of_type
is_any_type = is_any_values_of_type
is_in = is_value_in_iterable
is_any_in = is_any_values_in_iterable
is_all_in = is_all_values_in_iterable


## --------------------------------------------------------------------------- #
##  `assert_*()` functions                                                  ####
## --------------------------------------------------------------------------- #


def assert_value_of_type(
    value: Any,
    check_type: Union[type, tuple[type, ...]],
) -> None:
    """
    !!! summary "Summary"
        Assert that a given value is of a specified type or types.

    ???+ info "Details"
        This function is used to assert that a given value matches a specified type or any of the types in a tuple of types. If the value does not match the specified type(s), a `#!py TypeError` is raised.

    Params:
        value (Any):
            The value to check.
        check_type (Union[type, tuple[type]]):
            The type or tuple of types to check against.

    Raises:
        (TypeError):
            If the value is not of the specified type or one of the specified types.

    ???+ example "Examples"

        Assert that a value is of a specific type:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> value = 42
        >>> check_type = int
        ```

        ```{.py .python linenums="1" title="Example 1: Assert that value is of type int"}
        >>> assert_value_of_type(value, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is of type `#!py int`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Assert that value is of type str"}
        >>> assert_value_of_type(value, str)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
          ...
        TypeError: Value '42' is not correct type: 'int'. Must be: 'str'
        ```
        !!! failure "Conclusion: The value is not of type `#!py str`."

        </div>

        ```{.py .python linenums="1" title="Example 3: Assert that value is of type int or float"}
        >>> assert_value_of_type(value, (int, float))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is of type `#!py int` or `#!py float`."

        </div>

        ```{.py .python linenums="1" title="Example 4: Assert that value is of type str or dict"}
        >>> assert_value_of_type(value, (str, dict))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
          ...
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


def assert_all_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...]],
) -> None:
    """
    !!! summary "Summary"
        Assert that all values in an iterable are of a specified type or types.

    ???+ info "Details"
        This function is used to assert that all values in a given iterable match a specified type or any of the types in a tuple of types. If any value does not match the specified type(s), a `#!py TypeError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type]]):
            The type or tuple of types to check against.

    Raises:
        (TypeError):
            If any value is not of the specified type or one of the specified types.

    ???+ example "Examples"

        Assert that all values in an iterable are of a specific type:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 2, 3]
        >>> check_type = int
        ```

        ```{.py .python linenums="1" title="Example 1: Assert that all values are of type int"}
        >>> assert_all_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: All values are of type `#!py int`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Assert that all values are of type str"}
        >>> assert_all_values_of_type(values, str)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
        TypeError: Some elements [1, 2, 3] have the incorrect type ['int', 'int', 'int']. Must be 'str'
        ```
        !!! failure "Conclusion: Not all values are of type `#!py str`."

        </div>

        ```{.py .python linenums="1" title="Example 3: Assert that all values are of type int or float"}
        >>> assert_all_values_of_type(values, (int, float))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: All values are of type `#!py int` or `#!py float`."

        </div>

        ```{.py .python linenums="1" title="Example 4: Assert that all values are of type str or dict"}
        >>> assert_all_values_of_type(values, (str, dict))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
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
        invalid_types = [
            f"'{type(value).__name__}'"
            for value in values
            if not is_type(value, check_type)
        ]
        msg: str = (
            f"Some elements {invalid_values} have the incorrect type {invalid_types}. "
        )
        if isinstance(check_type, type):
            msg += f"Must be '{check_type}'"
        else:
            types: list[str] = [f"'{typ.__name__}'" for typ in check_type]
            msg += f"Must be: {' or '.join(types)}"
        raise TypeError(msg)


def assert_any_values_of_type(
    values: any_collection,
    check_type: Union[type, tuple[type, ...]],
) -> None:
    """
    !!! summary "Summary"
        Assert that any value in an iterable is of a specified type or types.

    ???+ info "Details"
        This function is used to assert that at least one value in a given iterable matches a specified type or any of the types in a tuple of types. If none of the values match the specified type(s), a `#!py TypeError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        check_type (Union[type, tuple[type]]):
            The type or tuple of types to check against.

    Raises:
        (TypeError):
            If none of the values are of the specified type or one of the specified types.

    ???+ example "Examples"

        Assert that any value in an iterable is of a specific type:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 'a', 3.0]
        >>> check_type = str
        ```

        ```{.py .python linenums="1" title="Example 1: Assert that any value is of type str"}
        >>> assert_any_values_of_type(values, check_type)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: At least one value is of type `#!py str`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Assert that any value is of type dict"}
        >>> assert_any_values_of_type(values, dict)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
        TypeError: None of the elements in [1, 'a', 3.0] have the correct type. Must be: 'dict'
        ```
        !!! failure "Conclusion: None of the values are of type `#!py dict`."

        </div>

        ```{.py .python linenums="1" title="Example 3: Assert that any value is of type int or float"}
        >>> assert_any_values_of_type(values, (int, float))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: At least one value is of type `#!py int` or `#!py float`."

        </div>

        ```{.py .python linenums="1" title="Example 4: Assert that any value is of type dict or list"}
        >>> assert_any_values_of_type(values, (dict, list))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
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
            types: list[str] = [f"'{typ.__name__}'" for typ in check_type]
            msg += f"Must be: {' or '.join(types)}"
        raise TypeError(msg)


def assert_value_in_iterable(
    value: scalar,
    iterable: any_collection,
) -> None:
    """
    !!! summary "Summary"
        Assert that a given value is present in an iterable.

    ???+ info "Details"
        This function is used to assert that a given value exists within an iterable such as a `#!py list`, `#!py tuple`, or `#!py set`. If the value is not found in the iterable, a `#!py LookupError` is raised.

    Params:
        value (scalar):
            The value to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (LookupError):
            If the value is not found in the iterable.

    ???+ example "Examples"

        Assert that a value is in an iterable:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> value = 2
        >>> iterable = [1, 2, 3]
        ```

        ```{.py .python linenums="1" title="Example 1: Assert that value is in the iterable"}
        >>> assert_value_in_iterable(value, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: The value is in the iterable."

        </div>

        ```{.py .python linenums="1" title="Example 2: Assert that value is not in the iterable"}
        >>> assert_value_in_iterable(4, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
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
    !!! summary "Summary"
        Assert that any value in an iterable is present in another iterable.

    ???+ info "Details"
        This function is used to assert that at least one value in a given iterable exists within another iterable. If none of the values are found in the iterable, a `#!py LookupError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (LookupError):
            If none of the values are found in the iterable.

    ???+ example "Examples"

        Assert that any value in an iterable is present in another iterable:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 4]
        >>> iterable = [1, 2, 3]
        ```

        ```{.py .python linenums="1" title="Example 1: Assert that any value is in the iterable"}
        >>> assert_any_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: At least one value is in the iterable."

        </div>

        ```{.py .python linenums="1" title="Example 2: Assert that any value is not in the iterable"}
        >>> assert_any_values_in_iterable([4, 5], iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
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
    !!! summary "Summary"
        Assert that all values in an iterable are present in another iterable.

    ???+ info "Details"
        This function is used to assert that all values in a given iterable exist within another iterable. If any value is not found in the iterable, a `#!py LookupError` is raised.

    Params:
        values (any_collection):
            The iterable containing values to check.
        iterable (any_collection):
            The iterable to check within.

    Raises:
        (LookupError):
            If any value is not found in the iterable.

    ???+ example "Examples"

        Assert that all values in an iterable are present in another iterable:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> values = [1, 2]
        >>> iterable = [1, 2, 3]
        ```

        ```{.py .python linenums="1" title="Example 1: Assert that all values are in the iterable"}
        >>> assert_all_values_in_iterable(values, iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        (no output, no exception raised)
        ```
        !!! success "Conclusion: All values are in the iterable."

        </div>

        ```{.py .python linenums="1" title="Example 2: Assert that all values are not in the iterable"}
        >>> assert_all_values_in_iterable([1, 4], iterable)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        Traceback (most recent call last):
            ...
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


### Aliases ----
assert_type = assert_value_of_type
assert_all_type = assert_all_values_of_type
assert_any_type = assert_any_values_of_type
assert_in = assert_value_in_iterable
assert_any_in = assert_any_values_in_iterable
assert_all_in = assert_all_values_in_iterable


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
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if at least one element in `iterable` contains `check` string; `#!py False` if no elements contain `check`.

    ???+ example "Examples"

        Check if any element in an iterable contains a specific string:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> iterable = ["apple", "banana", "cherry"]
        >>> check = "an"
        ```

        ```{.py .python linenums="1" title="Example 1: Check if any element contains 'an'"}
        >>> any_element_contains(iterable, check)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: At least one element contains `'an'`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if any element contains 'xy'"}
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
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if all elements in `iterable` contains `check` string; `#!py False` otherwise.

    ???+ example "Examples"

        Check if all elements in an iterable contain a specific string:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> iterable = ["apple", "banana", "peach"]
        >>> check = "a"
        ```

        ```{.py .python linenums="1" title="Example 1: Check if all elements contain 'a'"}
        >>> all_elements_contains(iterable, check)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        True
        ```
        !!! success "Conclusion: All elements contain `'a'`."

        </div>

        ```{.py .python linenums="1" title="Example 2: Check if all elements contain 'e'"}
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
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (tuple):
            A `#!py tuple` containing all the string elements from `iterable` which contains the `check` string.

    ???+ example "Examples"

        Extract elements in an iterable that contain a specific string:

        ```{.py .python linenums="1" title="Prepare data"}
        >>> iterable = ["apple", "banana", "cherry"]
        >>> check = "an"
        ```

        ```{.py .python linenums="1" title="Example 1: Extract elements containing 'an'"}
        >>> get_elements_containing(iterable, check)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ('banana',)
        ```
        !!! success "Conclusion: The element(s) containing `'an'` are extracted."

        </div>

        ```{.py .python linenums="1" title="Example 2: Extract elements containing 'xy'"}
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
