# ============================================================================ #
#                                                                              #
#     Title   : Strings                                                        #
#     Purpose : Manipulate and check strings.                                  #
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
    The `strings` module is for manipulating and checking certain string objects.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import re
import string

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import str_list, str_list_tuple


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #

__all__: list[str] = [
    "str_replace",
    "str_contains",
    "str_contains_any",
    "str_contains_all",
    "str_separate_number_chars",
]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def str_replace(
    old_string: str,
    replace_chars: str = string.punctuation + string.whitespace,
    replace_with: str = "",
) -> str:
    """
    !!! note "Summary"
        Replace the characters with a given string.

    ???+ abstract "Details"
        Similar to the Python `#!py str.replace()` method, but provides more customisation through the use of the [`re`](https://docs.python.org/3/library/re.html) package.

    Params:
        old_string (str):
            The old string to be replaced.
        replace_chars (str):
            The characters that need replacing.<br>
            Defaults to `#!py string.punctuation + string.whitespace`.
        replace_with (str):
            The value to replace the characters with.<br>
            Defaults to `""`.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (str):
            The new formatted string.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    !!! success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python#answer-23996414

    !!! tip "See Also"
        - [`re`](https://docs.python.org/3/library/re.html)
    """
    chars: str = re.escape(replace_chars)
    return re.sub(rf"[{chars}]", replace_with, old_string)


@typechecked
def str_contains(check_string: str, sub_string: str) -> bool:
    """
    !!! note "Summary"
        Check whether one string contains another string.

    ???+ abstract "Details"
        Super simple execution:
        ```py linenums="1"
        return True if sub_string in check_string else False
        ```

    Params:
        check_string (str):
            The main string to check.
        sub_string (str):
            The substring to check.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if `#!py sub_string` in `#!py check_string`

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    ??? tip "See Also"
        - [`str_contains_any()`][python_helpers.strings.str_contains_any]
        - [`str_contains_all()`][python_helpers.strings.str_contains_all]
    """
    return sub_string in check_string


@typechecked
def str_contains_any(
    check_string: str,
    sub_strings: str_list_tuple,
) -> bool:
    """
    !!! note "Summary"
        Check whether any one of a number of strings are contained within a main string.

    Params:
        check_string (str):
            The main string to check.
        sub_strings (Union[Tuple[str, ...], List[str]]):
            The collection of substrings to check.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if `#!py any` of the strings in `#!py sub_strings` are contained within `#!py check_string`.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    ??? tip "See Also"
        - [`str_contains()`][python_helpers.strings.str_contains]
        - [`str_contains_all()`][python_helpers.strings.str_contains_all]
    """
    return any(
        str_contains(
            check_string=check_string,
            sub_string=sub_string,
        )
        for sub_string in sub_strings
    )


@typechecked
def str_contains_all(
    check_string: str,
    sub_strings: str_list_tuple,
) -> bool:
    """
    !!! note "Summary"
        Check to ensure that all sub-strings are contained within a main string.

    Params:
        check_string (str):
            The main string to check.
        sub_strings (Union[Tuple[str, ...], List[str]]):
            The collection of substrings to check.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if `#!py all` of the strings in `#!py sub_strings` are contained within `#!py check_string`.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    ??? tip "See Also"
        - [`str_contains()`][python_helpers.strings.str_contains]
        - [`str_contains_any()`][python_helpers.strings.str_contains_any]
    """
    return all(
        str_contains(
            check_string=check_string,
            sub_string=sub_string,
        )
        for sub_string in sub_strings
    )


def str_separate_number_chars(text: str) -> str_list:
    """
    !!! note "Summary"
        Take in a string that contains both numbers and letters, and output a list of strings, separated to have each element containing either entirely number or entirely letters.

    ???+ abstract "Details"
        Uses regex ([`re.split()`](https://docs.python.org/3/library/re.html#re.split)) to perform the actual splitting.<br>
        Note, it _will_ preserve special characters & punctuation, but it _will not_ preserve whitespaces.

    Params:
        text (str):
            The string to split.

    Returns:
        (List[str]):
            The updated list, with each element of the list containing either entirely characters or entirely numbers.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    !!! success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/3340081/product-code-looks-like-abcd2343-how-to-split-by-letters-and-numbers#answer-63362709.

    ??? tip "See Also"
        - [`re`](https://docs.python.org/3/library/re.html)
    """
    res = re.split(r"([-+]?\d+\.\d+)|([-+]?\d+)", text.strip())
    return [r.strip() for r in res if r is not None and r.strip() != ""]
