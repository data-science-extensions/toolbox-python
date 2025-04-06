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
from toolbox_python.checkers import assert_type
from toolbox_python.collection_types import (
    dict_int_str,
    dict_str_any,
    dict_str_int,
    dict_str_str,
    int_list,
    int_tuple,
    str_list,
    str_tuple,
)

# Local Module Imports
from toolbox_python.dictionaries import DotDict, dict_reverse_keys_and_values


# ---------------------------------------------------------------------------- #
#                                                                              #
#     dict_reverse_keys_and_values()                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestDictReverseKeysAndValues(TestCase):

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


# ---------------------------------------------------------------------------- #
#                                                                              #
#     DotDict()                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestDotDict(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_dict: dict_str_any = {
            "version": 1.0,
            "title": "Sample Dictionary",
            "user": {
                "name": "John",
                "age": 30,
                "address": {"city": "New York", "zip": "10001"},
            },
            "list_objects": [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}],
            "tuple_objects": (1, 2, 3, 4, 5, 6),
            "set_objects": {"a", "b", "c", "d", "e", "f"},
        }
        cls.dot_dict = DotDict(cls.test_dict)

    def test_dict_init(self) -> None:
        assert_type(self.dot_dict, DotDict)
        assert_type(self.dot_dict, dict)

    def test_dict_values(self) -> None:
        assert self.dot_dict.version == 1.0
        assert self.dot_dict.title == "Sample Dictionary"
        with pytest.raises(AttributeError):
            assert self.dot_dict.missing == "Missing Key"

    def test_dict_nested_values(self) -> None:
        assert self.dot_dict.user.name == "John"
        assert self.dot_dict.user.age == 30
        assert self.dot_dict.user.address.city == "New York"
        assert self.dot_dict.user.address.zip == "10001"

    def test_dict_list_values(self) -> None:
        assert self.dot_dict.list_objects[0].id == 1
        assert self.dot_dict.list_objects[0].name == "Item 1"
        assert self.dot_dict.list_objects[1].id == 2
        assert self.dot_dict.list_objects[1].name == "Item 2"
        assert self.dot_dict.tuple_objects[0] == 1
        assert self.dot_dict.tuple_objects[1] == 2
        assert self.dot_dict.tuple_objects == self.test_dict["tuple_objects"]
        assert self.dot_dict.set_objects == self.test_dict["set_objects"]

    def test_dict_standard_usage(self) -> None:
        assert self.dot_dict["version"] == 1.0
        assert self.dot_dict["title"] == "Sample Dictionary"
        assert self.dot_dict["user"]["name"] == "John"
        assert self.dot_dict["user"]["age"] == 30
        assert self.dot_dict["user"]["address"]["city"] == "New York"
        assert self.dot_dict["user"]["address"]["zip"] == "10001"
        assert self.dot_dict["list_objects"][0]["id"] == 1
        assert self.dot_dict["list_objects"][0]["name"] == "Item 1"
        assert self.dot_dict["list_objects"][1]["id"] == 2
        assert self.dot_dict["list_objects"][1]["name"] == "Item 2"

    def test_dict_add_new_key(self) -> None:
        self.dot_dict.key_one = "New Value"
        assert self.dot_dict.key_one == "New Value"
        del self.dot_dict.key_one
        self.dot_dict["key_two"] = "New Value"
        assert self.dot_dict["key_two"] == "New Value"
        del self.dot_dict["key_two"]
        with pytest.raises(KeyError):
            del self.dot_dict["missing_key"]
        with pytest.raises(AttributeError):
            del self.dot_dict.missing_key

    def test_convert_to_dict(self) -> None:
        dict_from_dotdict = self.dot_dict.to_dict()
        assert isinstance(dict_from_dotdict, dict)
        assert dict_from_dotdict == self.test_dict
        assert dict_from_dotdict["user"]["name"] == "John"
        assert dict_from_dotdict["list_objects"][0]["name"] == "Item 1"
        with pytest.raises(AttributeError):
            dict_from_dotdict.version
            dict_from_dotdict.title

    def test_update_dict(self) -> None:
        new_dict = {
            "version": 2.0,
            "title": "Updated Dictionary",
            "user": {"name": "Jane", "age": 25},
        }
        self.dot_dict.update(new_dict)
        assert self.dot_dict.version == 2.0
        assert self.dot_dict.title == "Updated Dictionary"
        assert self.dot_dict.user.name == "Jane"
        assert self.dot_dict.user.age == 25
