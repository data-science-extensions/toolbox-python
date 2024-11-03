# ============================================================================ #
#                                                                              #
#     Title   : Bools                                                          #
#     Purpose : Manipulate and enhance booleans.                               #
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
    The `bools` module is used how to manipulate and enhance Python booleans.
!!! abstract "Details"
    Primarily, this module is used to store the `strtobool()` function, which used to be found in the `distutils.util` module, until it was deprecated. As mentioned in [PEP632](https://peps.python.org/pep-0632/#migration-advice), we should re-implement this function in our own code. And that's what we've done here.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #


__all__: list[str] = ["strtobool", "STR_TO_BOOL_MAP"]


# ---------------------------------------------------------------------------- #
#  Constants                                                                ####
# ---------------------------------------------------------------------------- #


STR_TO_BOOL_MAP: dict[str, bool] = {
    "y": True,
    "yes": True,
    "t": True,
    "true": True,
    "on": True,
    "1": True,
    "n": False,
    "no": False,
    "f": False,
    "false": False,
    "off": False,
    "0": False,
}
"""
Summary:
    Map of string values to their corresponding boolean values.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


def strtobool(value: str) -> bool:
    """
    !!! note "Summary"
        Convert a `#!py str` value in to a `#!py bool` value.

    ???+ abstract "Details"
        This process is necessary because the `d`istutils` module was completely deprecated in Python 3.12.

    Params:
        value (str):
            The string value to convert. Valid input options are defined in [`STR_TO_BOOL_MAP`][toolbox_python.bools.STR_TO_BOOL_MAP]

    Raises:
        ValueError:
            If the value parse'ed in to `value` is not a valid value to be able to convert to a `#!py bool` value.

    Returns:
        (bool):
            A `#!py True` or `#!py False` value, having successfully converted `value`.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        from toolbox_python.bools import strtobool
        ```

        ```{.py .python linenums="1" title="Example 1: `true` conversions"}
        >>> print(strtobool("true"))
        >>> print(strtobool("t"))
        >>> print(strtobool("1"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        True
        True
        True
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 2: `false` conversions"}
        >>> print(strtobool("false"))
        >>> print(strtobool("f"))
        >>> print(strtobool("0"))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        False
        False
        False
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 3: invalid value"}
        >>> print(strtobool(5))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        ValueError: Invalid bool value: '5'.
        For `True`, must be one of: ['y', 'yes', 't', 'true', 'on', '1']
        For `False`, must be one of: ['n', 'no', 'f', 'false', 'off', '0']
        ```
        !!! failure "Conclusion: Invalid type."
        </div>

    ??? question "References"
        - [PEP632](https://peps.python.org/pep-0632/#migration-advice)
    """
    try:
        return STR_TO_BOOL_MAP[str(value).lower()]
    except KeyError as exc:
        raise ValueError(
            f"Invalid bool value: '{value}'.\n"
            f"For `True`, must be one of: {[key for key, val in STR_TO_BOOL_MAP.items() if val]}\n"
            f"For `False`, must be one of: {[key for key, val in STR_TO_BOOL_MAP.items() if not val]}"
        ) from exc
