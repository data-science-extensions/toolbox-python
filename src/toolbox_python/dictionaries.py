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
    Note that functions in this module will only take-in and manipulate existing `#!py dict` objects, and also output `#!py dict` objects. It will not sub-class the base `#!py dict` object, or create new '`#!py dict`-like' objects. It will always maintain pure python types at it's core.
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
        This process is simple enough if the `values` are atomic types, like `#!py str`, `#!py int`, or `#!py float` types. But it is a little more tricky when the `values` are more complex types, like `#!py list` or `#!py dict`; here we need to use some recursion.

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

        ```{.py .python linenums="1" title="Set up"}
        >>> # Imports
        >>> from toolbox_python.dictionaries import dict_reverse_keys_and_values
        >>>
        >>> # Basic dictionary
        >>> dict_basic = {
        ...     "a": 1,
        ...     "b": 2,
        ...     "c": 3,
        ... }
        >>>
        >>> # Dictionary with iterables
        >>> dict_iterables = {
        ...     "a": ["1", "2", "3"],
        ...     "b": [4, 5, 6],
        ...     "c": ("7", "8", "9"),
        ...     "d": (10, 11, 12),
        ... }
        >>>
        >>> # Dictionary with iterables and duplicates
        >>> dict_iterables_with_duplicates = {
        ...     "a": [1, 2, 3],
        ...     "b": [4, 2, 5],
        ... }
        >>>
        >>> # Dictionary with sub-dictionaries
        >>> dict_with_dicts = {
        ...     "a": {
        ...         "aa": 11,
        ...         "bb": 22,
        ...         "cc": 33,
        ...     },
        ...     "b": {
        ...         "dd": [1, 2, 3],
        ...         "ee": ("4", "5", "6"),
        ...     },
        ... }
        ```

        ```{.py .python linenums="1" title="Example 1: Reverse one-for-one"}
        >>> print(dict_reverse_keys_and_values(dict_basic))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        {
            "1": "a",
            "2": "b",
            "3": "c",
        }
        ```
        !!! success "Conclusion: Successful conversion."
        !!! observation "Notice here that the original values were type `#!py int`, but here they have been converted to `#!py str`. This is because `#!py dict` keys should ideally only be `#!py str` type."
        </div>

        ```{.py .python linenums="1" title="Example 2: Reverse dictionary containing iterables in `values`"}
        >>> print(dict_reverse_keys_and_values(dict_iterables))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        {
            "1": "a",
            "2": "a",
            "3": "a",
            "4": "b",
            "5": "b",
            "6": "b",
            "7": "c",
            "8": "c",
            "9": "c",
            "10": "d",
            "11": "d",
            "12": "d",
        }
        ```
        !!! success "Conclusion: Successful conversion."
        !!! observation "Notice here how it has 'flattened' the iterables in the `values` in to individual keys, and assigned the original `key` to multiple keys. They keys have again been coerced to `#!py str` type."
        </div>

        ```{.py .python linenums="1" title="Example 3: Dictionary with iterables, raise error when `key` already exists"}
        >>> print(dict_reverse_keys_and_values(dict_iterables_with_duplicates))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        KeyError: Key already existing.
        Cannot update `output_dict` with new elements: {2: 'b'}
        Because the key is already existing for: {'2': 'a'}
        Full `output_dict` so far:
        {'1': 'a', '2': 'a', '3': 'a', '4': 'b'}
        ```
        !!! failure "Conclusion: Failed conversion."
        !!! observation "Here, in the second element of the dictionary (`#!py "b"`), there is a duplicate value `#!py 2` which is already existing in the first element of the dictionary (`#!py "a"`). So, we would expect to see an error.<br>Remember, a Python `#!py dict` object _cannot_ contain duplicate keys. They must always be unique."
        </div>

        ```{.py .python linenums="1" title="Example 4: Dictionary with embedded dictionaries"}
        >>> print(dict_reverse_keys_and_values(dict_with_dicts))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        {
            "1": "a",
            "2": "a",
            "3": "a",
            "4": "b",
            "5": "b",
            "6": "b",
            "7": "c",
            "8": "c",
            "9": "c",
            "10": "d",
            "11": "d",
            "12": "d",
        }
        ```
        !!! success "Conclusion: Successful conversion."
        !!! observation "Here, the process would be to run a recursive process when it recognises that any `value` is a `#!py dict` object. So long as there are no duplicate values in any of the contained `#!py dict`'s, the resulting output will be a big, flat dictionary."
        </div>
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
