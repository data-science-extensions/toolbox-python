# ============================================================================ #
#                                                                              #
#     Title   : Dictionaries                                                   #
#     Purpose : Manipulate and enhance dictionaries.                           #
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
    The `dictionaries` module is used how to manipulate and enhance Python dictionaries.
!!! abstract "Details"
    Note that functions in this module will only take-in and manipulate existing `#!py dict` objects, and also output `#!py dict` objects. It will not sub-class the base `#!py dict` object, or create new '`#!py dict`-like' objects. It will always remain pure python types at it's core.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import dict_any, dict_str_int


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #

__all__: list[str] = ["dict_reverse_keys_and_values"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def dict_reverse_keys_and_values(
    dictionary: dict_any,
) -> dict_str_int:
    """
    !!! note "Summary"
        Take the `key` and `values` of a dictionary, and reverse them.

    ???+ info "Details"
        This process is simple enough if the `values` are atomic types, like `#!py str`, `#!py int`, or `#!py float` types. But it is a little more tricky when the `values` are more comples types, like `#!py list` or `#!py dict`; here we need to use some recursion.

    Params:
        dictionary (dict_any):
            The input `#!py dict` that you'd like to have the `keys` and `values` switched.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        KeyError: When there are duplicate `values` being coerced to `keys` in the new dictionary. Raised because a Python `#!py dict` cannot have duplicate keys of the same value.

    Returns:
        output_dict (dict_str_int):
            The updated `#!py dict`.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)
    """
    output_dict: dict_str_int = dict()
    for key, value in dictionary.items():
        if isinstance(value, (str, int, float)):
            output_dict[str(value)] = key
        elif isinstance(value, (tuple, list)):
            for elem in value:
                if str(elem) in output_dict.keys():
                    raise KeyError(
                        f"Key already existing.\n"
                        f"Cannot update `output_dict` with new elements: { {elem: key} }\n"
                        f"Because the key is already existing for: { {new_key: new_value for (new_key, new_value) in output_dict.items() if new_key==str(elem)} }\n"
                        f"Full `output_dict` so far:\n{output_dict}"
                    )
                output_dict[str(elem)] = key
        elif isinstance(value, dict):
            interim_dict: dict_str_int = dict_reverse_keys_and_values(value)
            output_dict = {
                **output_dict,
                **interim_dict,
            }
    return output_dict
