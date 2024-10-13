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
    print_or_log: Optional[Literal["print", "log"]] = "print",
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
            if `#!py print_or_log=="log"`, then this parameter must contain the required log level for the `message`.
            Must be one of the log-levels available in the `#!py logging` module.<br>
            Defaults to `#!py None`.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        AssertError: If `#!py print_or_log=="log"` and `#!py log` is not an instance of `#!py Logger`.

    Returns:
        (None):
            Nothing is returned. Only printed or logged.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    """
    if print_or_log == "print":
        print(message)
    elif print_or_log == "log":
        if not is_type(log, Logger):
            raise TypeError(
                f"When `print_or_log=='log'` then `log` must be type `Logger`. Here, you have parsed: '{type(log)}'"
            )
        if log_level is None:
            raise ValueError(
                f"When `print_or_log=='log'` then `log_level` must be parsed with a valid value from: {log_levels}."
            )
        assert log is not None
        assert log_level is not None
        log.log(
            level=_nameToLevel[log_level.upper()],
            msg=message,
        )
    else:
        return None


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
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        printer (Optional[str]):
            The formatted string object.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    ???+ Success "Credit"
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
