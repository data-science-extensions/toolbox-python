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


# ## Python StdLib Imports ----
from typing import Any

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import dict_any, dict_str_any, str_list


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #

__all__: str_list = ["dict_reverse_keys_and_values", "DotDict"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Swap Keys & Values                                                    ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def dict_reverse_keys_and_values(dictionary: dict_any) -> dict_str_any:
    """
    !!! note "Summary"
        Take the `key` and `values` of a dictionary, and reverse them.

    ???+ abstract "Details"
        This process is simple enough if the `values` are atomic types, like `#!py str`, `#!py int`, or `#!py float` types. But it is a little more tricky when the `values` are more complex types, like `#!py list` or `#!py dict`; here we need to use some recursion.

    Params:
        dictionary (dict_any):
            The input `#!py dict` that you'd like to have the `keys` and `values` switched.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        (KeyError):
            When there are duplicate `values` being coerced to `keys` in the new dictionary. Raised because a Python `#!py dict` cannot have duplicate keys of the same value.

    Returns:
        output_dict (dict_str_int):
            The updated `#!py dict`.

    ???+ example "Examples"

        ```pycon {.py .python linenums="1" title="Set up"}
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

        ```pycon {.py .python linenums="1" title="Example 1: Reverse one-for-one"}
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

        ```pycon {.py .python linenums="1" title="Example 2: Reverse dictionary containing iterables in `values`"}
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

        ```pycon {.py .python linenums="1" title="Example 3: Dictionary with iterables, raise error when `key` already exists"}
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

        ```pycon {.py .python linenums="1" title="Example 4: Dictionary with embedded dictionaries"}
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
    output_dict: dict_str_any = dict()
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
            interim_dict: dict_str_any = dict_reverse_keys_and_values(value)
            output_dict = {
                **output_dict,
                **interim_dict,
            }
    return output_dict


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Use dot-methods to access values                                      ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class DotDict(dict):
    """
    !!! note "Summary"
        Dictionary subclass that allows dot notation access to keys.

    !!! abstract "Details"
        Nested dictionaries are automatically converted to DotDict instances.

    ???+ example "Examples"
        ```pycon {.py .python linenums="1" title="Set up"}
        >>> # Imports
        >>> from toolbox_python.dictionaries import DotDict
        >>>
        >>> # Create a DotDict
        >>> dot_dict = DotDict({"a": 1, "b": {"c": 2}})
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Accessing values with dot notation"}
        >>> print(dot_dict.a)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        1
        ```
        !!! success "Conclusion: Successfully accessed value using dot notation."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Accessing nested values with dot notation"}
        >>> print(dot_dict.b.c)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        2
        ```
        !!! success "Conclusion: Successfully accessed nested value using dot notation."
        </div>

        ```pycon {.py .python linenums="1" title="Example 3: Setting values with dot notation"}
        >>> dot_dict.d = 3
        >>> print(dot_dict.d)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        3
        ```
        !!! success "Conclusion: Successfully set value using dot notation."
        </div>

        ```pycon {.py .python linenums="1" title="Example 4: Updating nested values with dot notation"}
        >>> dot_dict.b.e = 4
        >>> print(dot_dict.b.e)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        4
        ```
        !!! success "Conclusion: Successfully updated nested value using dot notation."
        </div>

        ```pycon {.py .python linenums="1" title="Example 5: Converting back to regular dict"}
        >>> regular_dict = dot_dict.to_dict()
        >>> print(regular_dict)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        {'a': 1, 'b': {'c': 2, 'e': 4}, 'd': 3}
        ```
        !!! success "Conclusion: Successfully converted DotDict back to regular dict."
        </div>
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        dict.__init__(self)
        d = dict(*args, **kwargs)
        for key, value in d.items():
            self[key] = self._convert_value(value)

    def _convert_value(self, value: Any):
        """
        !!! note "Summary"
            Convert dictionary values recursively.

        Params:
            value (Any):
                The value to convert.

        Returns:
            (Any):
                The converted value.
        """
        if isinstance(value, dict):
            return DotDict(value)
        elif isinstance(value, list):
            return list(self._convert_value(item) for item in value)
        elif isinstance(value, tuple):
            return tuple(self._convert_value(item) for item in value)
        elif isinstance(value, set):
            return {self._convert_value(item) for item in value}
        return value

    def __getattr__(self, key: str) -> Any:
        """
        !!! note "Summary"
            Allow dictionary keys to be accessed as attributes.

        Params:
            key (str):
                The key to access.

        Raises:
            (AttributeError):
                If the key does not exist in the dictionary.

        Returns:
            (Any):
                The value associated with the key.
        """
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(f"Key not found: '{key}'") from e

    def __setattr__(self, key: str, value: Any) -> None:
        """
        !!! note "Summary"
            Allow setting dictionary keys via attributes.

        Params:
            key (str):
                The key to set.
            value (Any):
                The value to set.

        Returns:
            (None):
                This function does not return a value. It sets the key-value pair in the dictionary.
        """
        self[key] = value

    def __setitem__(self, key: str, value: Any) -> None:
        """
        !!! note "Summary"
            Intercept item setting to convert dictionaries.

        Params:
            key (str):
                The key to set.
            value (Any):
                The value to set.

        Returns:
            (None):
                This function does not return a value. It sets the key-value pair in the dictionary.
        """
        dict.__setitem__(self, key, self._convert_value(value))

    def __delitem__(self, key: str) -> None:
        """
        !!! note "Summary"
            Intercept item deletion to remove keys.

        Params:
            key (str):
                The key to delete.

        Raises:
            (KeyError):
                If the key does not exist in the dictionary.

        Returns:
            (None):
                This function does not return a value. It deletes the key-value pair from the dictionary.
        """
        try:
            dict.__delitem__(self, key)
        except KeyError as e:
            raise KeyError(f"Key not found: '{key}'.") from e

    def __delattr__(self, key: str) -> None:
        """
        !!! note "Summary"
            Allow deleting dictionary keys via attributes.

        Params:
            key (str):
                The key to delete.

        Raises:
            (AttributeError):
                If the key does not exist in the dictionary.

        Returns:
            (None):
                This function does not return a value. It deletes the key-value pair from the dictionary.
        """
        try:
            del self[key]
        except KeyError as e:
            raise AttributeError(f"Key not found: '{key}'") from e

    def update(self, *args: Any, **kwargs: Any) -> None:
        """
        !!! note "Summary"
            Override update to convert new values.

        Params:
            args (Any):
                Variable length argument list.
            kwargs (Any):
                Arbitrary keyword arguments.

        Returns:
            (None):
                This function does not return a value. It updates the dictionary with new key-value pairs.

        ???+ example "Examples"
            ```pycon {.py .python linenums="1" title="Update DotDict"}
            >>> dot_dict = DotDict({"a": 1, "b": 2})
            >>> dot_dict.update({"c": 3, "d": {"e": 4}})
            >>> print(dot_dict)
            ```
            <div class="result" markdown>
            ```{.sh .shell title="Output"}
            {'a': 1, 'b': 2, 'c': 3, 'd': {'e': 4}}
            ```
            !!! success "Conclusion: Successfully updated DotDict with new values."
            </div>
        """
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def to_dict(self) -> Any:
        """
        !!! note "Summary"
            Convert back to regular dictionary.

        Returns:
            (Any):
                The original dictionary structure, with all nested `#!py DotDict` instances converted back to regular dictionaries.

        ???+ example "Examples"
            ```pycon {.py .python linenums="1" title="Convert DotDict to regular dict"}
            >>> dot_dict = DotDict({"a": 1, "b": {"c": 2}})
            >>> regular_dict = dot_dict.to_dict()
            >>> print(regular_dict)
            ```
            <div class="result" markdown>
            ```{.sh .shell title="Output"}
            {'a': 1, 'b': {'c': 2}}
            ```
            !!! success "Conclusion: Successfully converted DotDict back to regular dict."
            </div>
        """

        def _convert_back(obj) -> Any:
            if isinstance(obj, DotDict):
                return {k: _convert_back(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return list(_convert_back(item) for item in obj)
            elif isinstance(obj, tuple):
                return tuple(_convert_back(item) for item in obj)
            elif isinstance(obj, set):
                return {_convert_back(item) for item in obj}
            return obj

        return _convert_back(self)
