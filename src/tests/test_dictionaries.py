# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from typing import Union
from unittest import TestCase

# ## Python Third Party Imports ----
import pytest

# ## Local First Party Imports ----
from toolbox_python.collection_types import (
    dict_int_str,
    dict_str_int,
    dict_str_str,
    int_list,
    int_tuple,
    str_list,
    str_tuple,
)

# Local Module Imports
from toolbox_python.dictionaries import dict_reverse_keys_and_values


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestDictionaries(TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.dict_basic: dict_str_int = {"a": 1, "b": 2, "c": 3}

        cls.dict_iterables: dict[
            str, Union[str_list, int_list, str_tuple, int_tuple]
        ] = {
            "a": ["1", "2", "3"],
            "b": [4, 5, 6],
            "c": ("7", "8", "9"),
            "d": (10, 11, 12),
        }

        cls.dict_iterables_with_duplicates: dict[str, int_list] = {
            "a": [1, 2, 3],
            "b": [4, 2, 5],
        }

        cls.dict_with_dicts: dict[str, dict[str, Union[int, int_list, str_tuple]]] = {
            "a": {
                "aa": 11,
                "bb": 22,
                "cc": 33,
            },
            "b": {
                "dd": [1, 2, 3],
                "ee": ("4", "5", "6"),
            },
        }

        cls.dict_with_repeats: dict[str, Union[int_list, str_tuple]] = {
            "a": [1, 1, 1, 1],
            "b": ("c", "c", "c"),
        }

    def test_reverse_dict_one_for_one(self) -> None:
        _input = self.dict_basic
        _output: dict_int_str = dict_reverse_keys_and_values(_input)
        _expected: dict_str_str = {"1": "a", "2": "b", "3": "c"}
        assert _output == _expected

    def test_reverse_dict_iterables(self) -> None:
        _input = self.dict_iterables
        _output = dict_reverse_keys_and_values(_input)
        _expected = {
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
        assert _output == _expected

    def test_reverse_dict_iterables_with_duplicates(self) -> None:
        _input = self.dict_iterables_with_duplicates
        _expected = (
            r"Key already existing.\n"
            r"Cannot update `output_dict` with new elements: {2: 'b'}\n"
            r"Because the key is already existing for: {'2': 'a'}\n"
            r"Full `output_dict` so far:\n"
            r"{'1': 'a', '2': 'a', '3': 'a', '4': 'b'}"
        )
        with pytest.raises(KeyError) as execinfo:
            _output = dict_reverse_keys_and_values(_input)
        assert str(execinfo.value) == f'"{_expected}"'

    def test_reverse_dict_embedded_dicts(self) -> None:
        _input = self.dict_with_dicts
        _output = dict_reverse_keys_and_values(_input)
        _expected: dict_str_str = {
            "11": "aa",
            "22": "bb",
            "33": "cc",
            "1": "dd",
            "2": "dd",
            "3": "dd",
            "4": "ee",
            "5": "ee",
            "6": "ee",
        }
        assert _output == _expected
