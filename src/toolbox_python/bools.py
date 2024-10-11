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
#  Constants                                                                ####
# ---------------------------------------------------------------------------- #


_MAP: dict[str, bool] = {
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


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #


__all__: list[str] = ["strtobool"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


def strtobool(value: str) -> bool:
    """
    !!! note "Summary"
        Convert a `#!py str` in to a `#!py bool` value.

    ???+ abstract "Details"
        This process is necessary because the `distutils` module was completely deprecated in Python 3.12.

    Params:
        value (str):
            The string value to convert. Valid input options are defined in [`_MAP`][python_helpers.bools._MAP]

    Raises:
        TypeError:
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        ValueError:
            If the value parse'ed in to `value` is not a valid value to be able to convert to a `#!py bool` value.

    Returns:
        (bool):
            A `#!py True` or `#!py False` value, having successfully converted `value`.

    ??? question "References"
        - [PEP632](https://peps.python.org/pep-0632/#migration-advice)
    """
    try:
        return _MAP[str(value).lower()]
    except KeyError as exc:
        raise ValueError(
            f"Invalid bool value: '{value}'.\n"
            f"For `True`, must be one of: {[key for key, val in _MAP.items() if val]}\n"
            f"For `False`, must be one of: {[key for key, val in _MAP.items() if not val]}"
        ) from exc
