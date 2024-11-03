# ============================================================================ #
#                                                                              #
#     Title   : Output                                                         #
#     Purpose : Streamline how data is outputted.                              #
#               Including `print`'ing and `logg`'ing                           #
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
    The `output` module is for streamlining how data is outputted.
    This includes `#!py print()`'ing to the terminal and `#!py log()`'ing to files.
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
from logging import Logger, _nameToLevel
from math import ceil
from typing import Any, Literal, Optional, Union

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.checkers import is_type
from toolbox_python.collection_types import log_levels, str_list


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #

__all__: str_list = ["print_or_log_output", "list_columns"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def print_or_log_output(
    message: str,
    print_or_log: Literal["print", "log"] = "print",
    log: Optional[Logger] = None,
    log_level: Optional[log_levels] = None,
) -> None:
    """
    !!! note "Summary"
        Determine whether to `#!py print()` or `#!py log()` a given `message`.

    Params:
        message (str):
            The `message` to be processed.
        print_or_log (Optional[Literal["print", "log"]], optional):
            The option for what to do with the `message`.<br>
            Defaults to `#!py "print"`.
        log (Optional[Logger], optional):
            If `#!py print_or_log=="log"`, then this parameter must contain the `#!py Logger` object to be processed,
            otherwise it will raise an `#!py AssertError`.<br>
            Defaults to `#!py None`.
        log_level (Optional[_log_levels], optional):
            If `#!py print_or_log=="log"`, then this parameter must contain the required log level for the `message`.
            Must be one of the log-levels available in the `#!py logging` module.<br>
            Defaults to `#!py None`.

    Raises:
        TypeError:
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        AssertError:
            If `#!py print_or_log=="log"` and `#!py log` is not an instance of `#!py Logger`.

    Returns:
        (None):
            Nothing is returned. Only printed or logged.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up data for examples"}
        >>> from toolbox_python.output import print_or_log_output
        >>> import logging
        >>> logging.basicConfig(filename="logs.log", encoding="utf-8")
        >>> log = logging.getLogger("root")
        >>> default_message = "This is a"
        ```

        ```{.py .python linenums="1" title="Example 1: Print output"}
        >>> print_or_log_output(
        ...     message=f"{default_message} print",
        ...     print_or_log="print",
        ... )
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        This is a print
        ```
        !!! success "Conclusion: Successfully printed the message."
        </div>

        ```{.py .python linenums="1" title="Example 2: Log `info`"}
        >>> print_or_log_output(
        ...     message=f"{default_message}n info",
        ...     print_or_log="log",
        ...     log=log,
        ...     log_level="info",
        ... )
        ```
        <div class="result" markdown>
        ```{.log .log title="logs.log"}
        INFO:root:This is an info
        ```
        !!! success "Conclusion: Successfully logged the message."
        </div>

        ```{.py .python linenums="1" title="Example 3: Log `debug`"}
        >>> print_or_log_output(
        ...     message=f"{default_message} debug",
        ...     print_or_log="log",
        ...     log=log,
        ...     log_level="debug",
        ... )
        ```
        <div class="result" markdown>
        ```{.log .log title="logs.log"}
        INFO:root:This is an info
        DEBUG:root:This is a debug
        ```
        !!! success "Conclusion: Successfully added message to logs."
        !!! observation "Note: This logging structure will continue for every new call to `print_or_log_output()` when `print_or_log="log"`, and the `log` and `log_level` parameters are valid."
        </div>

        ```{.py .python linenums="1" title="Example 7: Invalid `print_or_log` input"}
        >>> print_or_log_output(
        ...     message=f"{default_message} invalid",
        ...     print_or_log="error",
        ... )
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: `print_or_log` can only have the string values `"print"` or `"log"`."
        </div>

        ```{.py .python linenums="1" title="Example 8: Invalid `log` input"}
        >>> print_or_log_output(
        ...     message=f"{default_message} invalid",
        ...     print_or_log="log",
        ...     log=None,
        ...     log_level="info",
        ... )
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        AssertionError: When `print_or_log=='log'` then `log` must be type `Logger`. Here, you have parsed: '<class 'NoneType'>'
        ```
        !!! failure "Conclusion: When `print_or_log="log"` then `#!py log` must be an instance of `#!py Logger`."
        </div>

        ```{.py .python linenums="1" title="Example 9: Invalid `log_level` input"}
        >>> print_or_log_output(
        ...     message=f"{default_message} invalid",
        ...     print_or_log="log",
        ...     log=log,
        ...     log_level="invalid",
        ... )
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        TypeError: ...
        ```
        !!! failure "Conclusion: `log_level` must be a valid log level from the `logging` module."
        </div>
    """

    # Early exit when printing the message
    if print_or_log == "print":
        print(message)
        return None

    # Check in put for logging
    if not is_type(log, Logger):
        raise TypeError(
            f"When `print_or_log=='log'` then `log` must be type `Logger`. "
            f"Here, you have parsed: '{type(log)}'"
        )
    if log_level is None:
        raise ValueError(
            f"When `print_or_log=='log'` then `log_level` must be parsed "
            f"with a valid value from: {log_levels}."
        )

    # Assertions to keep `mypy` happy
    assert log is not None
    assert log_level is not None

    # Do logging
    log.log(
        level=_nameToLevel[log_level.upper()],
        msg=message,
    )


@typechecked
def list_columns(
    obj: list,
    cols_wide: int = 4,
    columnwise: bool = True,
    gap: int = 4,
    print_output: bool = True,
) -> Optional[str]:
    """
    !!! note Summary
        Print the given list in evenly-spaced columns.

    Params:
        obj (list):
            The list to be formatted.

        cols_wide (int, optional):
            The number of columns in which the list should be formatted.<br>
            Defaults to: `#!py 4`.

        columnwise (bool, optional):
            Whether or not to print columnwise or rowwise.

            - `#!py True`: Will be formatted column-wise.
            - `#!py False`: Will be formatted row-wise.

            Defaults to: `#!py True`.

        gap (int, optional):
            The number of spaces that should separate the longest column
            item/s from the next column. This is the effective spacing
            between columns based on the maximum `#!py len()` of the list items.<br>
            Defaults to: `#!py 4`.

        print_output (bool, optional):
            Whether or not to print the output to the terminal.

            - `#!py True`: Will print and return.
            - `#!py False`: Will not print; only return.

            Defaults to: `#!py True`.

    Raises:
        TypeError:
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        printer (Optional[str]):
            The formatted string object.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> # Imports
        >>> from toolbox_python.output import list_columns
        >>> import requests
        >>>
        >>> # Define function to fetch list of words
        >>> def get_list_of_words(num_words: int = 100):
        ...     word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
        ...     response = requests.get(word_url)
        ...     words = response.content.decode().splitlines()
        ...     return words[:num_words]
        ```

        ```{.py .python linenums="1" title="Example 1: Default parameters"}
        >>> list_columns(get_list_of_words(4 * 5))
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        a             abandoned     able          abraham
        aa            abc           aboriginal    abroad
        aaa           aberdeen      abortion      abs
        aaron         abilities     about         absence
        ab            ability       above         absent
        ```
        !!! success "Conclusion: Successfully printed the list in columns."
        </div>

        ```{.py .python linenums="1" title="Example 2: Columnwise with 2 columns"}
        >>> list_columns(
        ...     get_list_of_words(5),
        ...     cols_wide=2,
        ...     columnwise=True,
        ... )
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        a        aaron
        aa       ab
        aaa
        ```
        !!! success "Conclusion: Successfully printed the list in columns."
        </div>

        ```{.py .python linenums="1" title="Example 3: Rowwise with 3 columns"}
        >>> list_columns(
        ...     get_list_of_words(4 * 3),
        ...     columnwise=False,
        ...     cols_wide=3,
        ...     print_output=True,
        ... )
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        a             aa            aaa
        aaron         ab            abandoned
        abc           aberdeen      abilities
        ability       able          aboriginal
        ```
        !!! success "Conclusion: Successfully printed the list in rows."
        </div>

        ```{.py .python linenums="1" title="Example 4: Rowwise with 2 columns, no print output"}
        >>> output = list_columns(
        ...     get_list_of_words(4 * 2),
        ...     columnwise=False,
        ...     cols_wide=2,
        ...     print_output=False,
        ... )
        >>> print(output)
        ```
        <div class="result" markdown>
        ```{.txt .text title="Terminal"}
        a            aa
        aaa          aaron
        ab           abandoned
        abc          aberdeen
        ```
        !!! success "Conclusion: Successfully returned the formatted string."
        </div>

    ??? Success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/1524126/how-to-print-a-list-more-nicely#answer-36085705
    """
    string_list: list[str] = [str(item) for item in obj]
    if cols_wide > len(string_list):
        cols_wide = len(string_list)
    max_len: int = max(len(item) for item in string_list)
    if columnwise:
        cols_wide = int(ceil(len(string_list) / cols_wide))
    segmented_list: list[list[str]] = [
        string_list[index : index + cols_wide]
        for index in range(0, len(string_list), cols_wide)
    ]
    if columnwise:
        if len(segmented_list[-1]) != cols_wide:
            segmented_list[-1].extend(
                [""] * (len(string_list) - len(segmented_list[-1]))
            )
        combined_list: Union[list[list[str]], Any] = zip(*segmented_list)
    else:
        combined_list = segmented_list
    printer: str = "\n".join(
        [
            "".join([element.ljust(max_len + gap) for element in group])
            for group in combined_list
        ]
    )
    if print_output:
        print(printer)
    return printer
