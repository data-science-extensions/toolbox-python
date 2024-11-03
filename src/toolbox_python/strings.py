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
        replace_chars (str, optional):
            The characters that need replacing.<br>
            Defaults to `#!py string.punctuation + string.whitespace`.
        replace_with (str, optional):
            The value to replace the characters with.<br>
            Defaults to `""`.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (str):
            The new formatted string.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.strings import str_replace
        >>> long_string = "This long string"
        >>> complex_sentence = "Because my pizza was cold, I put it in the microwave."
        ```

        ```{.py .python linenums="1" title="Example 1: Replace all spaces (` `) with underscore (`_`)"}
        >>> print(str_replace(long_string, " ", "_"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        "This_long_string"
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 2: Remove all punctuation and white space"}
        >>> print(str_replace(complex_sentence))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        "BecausemylunchwascoldIputitinthemicrowave"
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 3: Invalid `old_string` input"}
        >>> print(str_replace(123))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: Invalid input."
        !!! observation "Note: The same error will occur if `replace_chars` or `replace_with` are not of type `str`."
        </div>

    ??? success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/23996118/replace-special-characters-in-a-string-python#answer-23996414

    ??? tip "See Also"
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
        This is a super simple one-line function.

        ```py linenums="1" title="Example"
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

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.strings import str_contains
        >>> long_string = "This long string"
        ```

        ```{.py .python linenums="1" title="Example 1: String is contained"}
        >>> print(str_contains(long_string, "long"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        True
        ```
        !!! success "Conclusion: `#!py long_string` contains `#!py "long"`."
        </div>

        ```{.py .python linenums="1" title="Example 2: String is not contained"}
        >>> print(str_contains(long_string, "short"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        False
        ```
        !!! success "Conclusion: `#!py long_string` does not contain `#!py "short"`."
        </div>

        ```{.py .python linenums="1" title="Example 3: Invalid `check_string` input"}
        >>> print(str_contains(123, "short"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: Invalid input."
        !!! observation "Note: The same error will occur if `sub_string` is not of type `str`."
        </div>

    ??? tip "See Also"
        - [`str_contains_any()`][toolbox_python.strings.str_contains_any]
        - [`str_contains_all()`][toolbox_python.strings.str_contains_all]
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
        sub_strings (str_list_tuple):
            The collection of substrings to check.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if `#!py any` of the strings in `#!py sub_strings` are contained within `#!py check_string`.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.strings import str_contains_any
        >>> long_string = "This long string"
        ```

        ```{.py .python linenums="1" title="Example 1: Contains any"}
        >>> print(str_contains_any(long_string, ["long", "short"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        True
        ```
        !!! success "Conclusion: `#!py long_string` contains either `#!py "long"` or `#!py "short"`."
        </div>

        ```{.py .python linenums="1" title="Example 2: Contains none"}
        >>> print(str_contains_any(long_string, ["this", "that"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        False
        ```
        !!! success "Conclusion: `#!py long_string` contains neither `#!py "this"` nor `#!py "that"`."
        </div>

        ```{.py .python linenums="1" title="Example 3: Invalid `check_string` input"}
        >>> print(str_contains_any(123, ["short", "long"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: Invalid input."
        !!! observation "Note: The same error will occur if any of the elements in `sub_strings` are not of type `str`."
        </div>

    ??? tip "See Also"
        - [`str_contains()`][toolbox_python.strings.str_contains]
        - [`str_contains_all()`][toolbox_python.strings.str_contains_all]
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
        sub_strings (str_list_tuple):
            The collection of substrings to check.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (bool):
            `#!py True` if `#!py all` of the strings in `#!py sub_strings` are contained within `#!py check_string`.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.strings import str_contains_all
        >>> long_string = "This long string"
        ```

        ```{.py .python linenums="1" title="Example 1: Contains all"}
        >>> print(str_contains_all(long_string, ["long", "string"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        True
        ```
        !!! success "Conclusion: `#!py long_string` contains both `#!py "long"` and `#!py "string"`."
        </div>

        ```{.py .python linenums="1" title="Example 2: Contains some"}
        >>> print(str_contains_all(long_string, ["long", "something"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        False
        ```
        !!! failure "Conclusion: `#!py long_string` contains `#!py "long"` but not `#!py "something"`."
        </div>

        ```{.py .python linenums="1" title="Example 3: Contains none"}
        >>> print(str_contains_all(long_string, ["this", "that"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        False
        ```
        !!! failure "Conclusion: `#!py long_string` contains neither `#!py "this"` nor `#!py "that"`."
        </div>

        ```{.py .python linenums="1" title="Example 4: Invalid `check_string` input"}
        >>> print(str_contains_all(123, ["short", "long"]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: Invalid input."
        !!! observation "Note: The same error will occur if any of the elements in `sub_strings` are not of type `str`."
        </div>

    ??? tip "See Also"
        - [`str_contains()`][toolbox_python.strings.str_contains]
        - [`str_contains_any()`][toolbox_python.strings.str_contains_any]
    """
    return all(
        str_contains(
            check_string=check_string,
            sub_string=sub_string,
        )
        for sub_string in sub_strings
    )


@typechecked
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

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (str_list):
            The updated list, with each element of the list containing either entirely characters or entirely numbers.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.strings import str_contains_all
        >>> simple_string = "-12.1grams"
        >>> complex_string = "abcd2343 abw34324 abc3243-23A 123"
        ```

        ```{.py .python linenums="1" title="Example 1: Simple split"}
        >>> print(str_separate_number_chars(simple_string))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        ["-12.1", "grams"]
        ```
        !!! success "Conclusion: Successful split."
        </div>

        ```{.py .python linenums="1" title="Example 2: Complex split"}
        >>> print(str_separate_number_chars(complex_string))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [
            "abcd",
            "2343",
            "abw",
            "34324",
            "abc",
            "3243",
            "-23",
            "A",
            "123",
        ]
        ```
        !!! success "Conclusion: Successful split."
        </div>

        ```{.py .python linenums="1" title="Example 3: `text` does not contain any numbers"}
        >>> print(str_separate_number_chars("abcd"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        ["abcd"]
        ```
        !!! success "Conclusion: No numbers in `#!py text`, so returns a single-element long list."
        </div>

        ```{.py .python linenums="1" title="Example 4: Invalid `text` input"}
        >>> print(str_separate_number_chars(123))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: Invalid input."
        </div>

    ??? success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/3340081/product-code-looks-like-abcd2343-how-to-split-by-letters-and-numbers#answer-63362709.

    ??? tip "See Also"
        - [`re`](https://docs.python.org/3/library/re.html)
    """
    res = re.split(r"([-+]?\d+\.\d+)|([-+]?\d+)", text.strip())
    return [r.strip() for r in res if r is not None and r.strip() != ""]
