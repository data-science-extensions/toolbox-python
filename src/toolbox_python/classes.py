# ============================================================================ #
#                                                                              #
#     Title   : Classes                                                        #
#     Purpose : Contain functions which can be run on classes to extract       #
#               general information.                                           #
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
    The `classes` module is designed for functions to be executed _on_ classes; not _within_ classes.
    For any methods/functions that should be added _to_ classes, you should consider re-designing the original class, or sub-classing it to make further alterations.
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
from typing import Any


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #


__all__: list[str] = ["get_full_class_name"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Name of classes                                                          ####
# ---------------------------------------------------------------------------- #


def get_full_class_name(obj: Any) -> str:
    """
    !!! note "Summary"
        This function is designed to extract the full name of a class, including the name of the module from which it was loaded.

    Params:
        obj (Any):
            The object for which you want to retrieve the full name.

    Returns:
        (str):
            The full name of the class of the object.

    !!! success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/18176602/how-to-get-the-name-of-an-exception-that-was-caught-in-python#answer-58045927

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)
    """
    module: str = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + "." + obj.__class__.__name__
