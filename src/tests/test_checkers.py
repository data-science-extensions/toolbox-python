# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from typing import Any, Union
from unittest import TestCase

# ## Python Third Party Imports ----
import pytest
from parameterized import parameterized

# ## Local First Party Imports ----
from tests.setup import name_func_nested_list, name_func_predefined_name
from toolbox_python.checkers import (
    all_elements_contains,
    any_element_contains,
    assert_all_in,
    assert_all_type,
    assert_all_values_in_iterable,
    assert_all_values_of_type,
    assert_any_in,
    assert_any_type,
    assert_any_values_in_iterable,
    assert_any_values_of_type,
    assert_in,
    assert_type,
    assert_value_in_iterable,
    assert_value_of_type,
    get_elements_containing,
    is_all_in,
    is_all_type,
    is_all_values_in_iterable,
    is_all_values_of_type,
    is_any_in,
    is_any_type,
    is_any_values_in_iterable,
    is_any_values_of_type,
    is_in,
    is_type,
    is_value_in_iterable,
    is_value_of_type,
)
from toolbox_python.collection_types import str_tuple


## --------------------------------------------------------------------------- #
##  Constants                                                               ####
## --------------------------------------------------------------------------- #


type_maps: dict[type, Any] = {
    str: "a",
    int: 1,
    float: 2.5,
    bool: True,
    tuple: (1, 2),
    list: ["a", "a"],
    set: {1.0, 1.0},
}


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Unit Tests                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestSuite(TestCase):

    def setUp(self) -> None:
        pass

    @parameterized.expand(
        (
            ("str_1", "a", str, True),
            ("str_2", 1, str, False),
            ("str_3", "a", (str, int), True),
            ("str_4", 2.5, (str, int), False),
            ("int_1", 1, int, True),
            ("int_2", "a", int, False),
            ("int_3", 1, (str, int), True),
            ("int_4", 2.5, (str, int), False),
            ("float_1", 2.5, float, True),
            ("float_2", "a", float, False),
            ("float_3", 2.5, (str, float), True),
            ("float_4", 1, (str, float), False),
            ("bool_1", True, bool, True),
            ("bool_2", "a", bool, False),
            ("bool_3", True, (str, bool), True),
            ("bool_4", 1, (str, bool), False),
            ("tuple_1", (1, 2), tuple, True),
            ("tuple_2", "a", tuple, False),
            ("tuple_3", (1, 2), (tuple, list), True),
            ("tuple_4", {"a", "b"}, (tuple, list), False),
            ("list_1", ["a", "a"], list, True),
            ("list_2", "a", list, False),
            ("list_3", ["a", "a"], (tuple, list), True),
            ("list_4", {1, 2}, (tuple, list), False),
            ("set_1", {1.0, 1.0}, set, True),
            ("set_2", "a", set, False),
            ("set_3", {1.0, 1.0}, (tuple, set), True),
            ("set_4", [1, 2], (tuple, set), False),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_value_of_type(
        self,
        _nam: str,
        _val: Any,
        _typ: Union[type, tuple[type, ...]],
        _res: bool,
    ) -> None:
        assert is_value_of_type(_val, _typ) == _res
        assert is_type(_val, _typ) == _res
        if _res:
            assert_type(_val, _typ)
            assert_value_of_type(_val, _typ)
        else:
            with pytest.raises(TypeError):
                assert_type(_val, _typ)
                assert_value_of_type(_val, _typ)

    @parameterized.expand(
        (
            ("str_1", ("a", "b", "c"), str, True),
            ("str_2", ("a", "b", 1), str, False),
            ("str_3", ("a", "b", "c"), (str, int), True),
            ("str_4", ("a", 1, "c"), (str, float), False),
            ("int_1", (1, 2, 3), int, True),
            ("int_2", (1, 2, 3.0), int, False),
            ("int_3", (1, 2, 3), (int, float), True),
            ("int_4", (1, 2.0, 3), (int, str), False),
            ("float_1", (1.0, 2.0, 3.0), float, True),
            ("float_2", (1.0, 2.0, 3), float, False),
            ("float_3", (1.0, 2.0, 3.0), (float, int), True),
            ("float_4", (1.0, 2, 3.0), (float, str), False),
            ("bool_1", (True, False, True), bool, True),
            ("bool_2", (True, False, 2.5), bool, False),
            ("bool_3", (True, False, True), (bool, float), True),
            ("bool_4", (True, 2.5, True), (bool, str), False),
            ("tuple_1", ((1, 2), (3, 4), (5, 6)), tuple, True),
            ("tuple_2", ((1, 2), (3, 4), [5, 6.0]), tuple, False),
            ("tuple_3", ((1, 2), (3, 4), (5, 6)), (tuple, list), True),
            ("tuple_4", ((1, 2), [3, 4], (5, 6)), (tuple, str), False),
            ("list_1", (["a", "b"], ["c", "d"], ["e", "f"]), list, True),
            ("list_2", (["a", "b"], ["c", "d"], {5, 6.0}), list, False),
            ("list_3", (["a", "b"], ["c", "d"], ["e", "f"]), (tuple, list), True),
            ("list_4", (["a", "b"], {3, 4}, ["e", "f"]), (tuple, str), False),
            ("set_1", ({1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0}), set, True),
            ("set_2", ({1.0, 2.0}, {3.0, 4.0}, [5.0, 6.0]), set, False),
            ("set_3", ({1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0}), (tuple, set), True),
            ("set_4", ({1.0, 2.0}, [3.0, 4.0], {5.0, 6.0}), (tuple, str), False),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_all_values_of_type(
        self,
        _nam: str,
        _vals: Any,
        _typ: Union[type, tuple[type, ...]],
        _res: bool,
    ) -> None:
        assert is_all_values_of_type(_vals, _typ) == _res
        assert is_all_type(_vals, _typ) == _res
        if _res:
            assert_all_values_of_type(_vals, _typ)
            assert_all_type(_vals, _typ)
        else:
            with pytest.raises(TypeError):
                assert_all_values_of_type(_vals, _typ)
                assert_all_type(_vals, _typ)

    @parameterized.expand(
        (
            ("str_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), str, True),
            ("str_2", (1, 2.5, True, (1, 2), [3, 4], {5, 6}), str, False),
            ("str_3", ("a", True, (1, 2), [3, 4], {5, 6}), (str, int), True),
            ("str_4", (2.5, (1, 2), [3, 4], {5, 6}), (str, int), False),
            ("int_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), int, True),
            ("int_2", ("a", 2.5, (1, 2), [3, 4], {5, 6}), int, False),
            ("int_3", (1, True, (1, 2), [3, 4], {5, 6}), (int, float), True),
            ("int_4", ("a", (1, 2), [3, 4], {5, 6}), (int, float), False),
            ("float_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), float, True),
            ("float_2", (1, "a", True, (1, 2), [3, 4], {5, 6}), float, False),
            ("float_3", (1, "a", 2.5, (1, 2), [3, 4], {5, 6}), (float, bool), True),
            ("float_4", (1, "a", [3, 4], {5, 6}), (float, bool), False),
            ("bool_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), bool, True),
            ("bool_2", (1, "a", 2.5, (1, 2), [3, 4], {5, 6}), bool, False),
            ("bool_3", (1, "a", True, (1, 2), [3, 4], {5, 6}), (bool, float), True),
            ("bool_4", (1, "a", (1, 2), [3, 4], {5, 6}), (bool, float), False),
            ("tuple_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), tuple, True),
            ("tuple_2", (1, "a", 2.5, True, [3, 4], {5, 6}), tuple, False),
            ("tuple_3", (1, "a", 2.5, True, (1, 2), {5, 6}), (tuple, list), True),
            ("tuple_4", (1, "a", 2.5, True, {5, 6}), (tuple, list), False),
            ("list_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), list, True),
            ("list_2", (1, "a", 2.5, True, (1, 2), {5, 6}), list, False),
            ("list_3", (1, "a", 2.5, True, [3, 4], {5, 6}), (list, tuple), True),
            ("list_4", (1, "a", 2.5, True, {5, 6}), (list, tuple), False),
            ("set_1", (1, "a", 2.5, True, (1, 2), [3, 4], {5, 6}), set, True),
            ("set_2", (1, "a", 2.5, True, (1, 2), [3, 4]), set, False),
            ("set_3", (1, "a", 2.5, True, (1, 2), {5, 6}), (set, list), True),
            ("set_4", (1, "a", 2.5, True, (1, 2)), (set, list), False),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_any_values_of_type(
        self,
        _nam: str,
        _vals: Any,
        _typ: Union[type, tuple[type, ...]],
        _res: bool,
    ) -> None:
        assert is_any_values_of_type(_vals, _typ) == _res
        assert is_any_type(_vals, _typ) == _res
        if _res:
            assert_any_values_of_type(_vals, _typ)
            assert_any_type(_vals, _typ)
        else:
            with pytest.raises(TypeError):
                assert_any_values_of_type(_vals, _typ)
                assert_any_type(_vals, _typ)

    @parameterized.expand(
        (
            ("list", ["a", "b", "c"]),
            ("tuple", (1, 2, 3)),
            ("set", {1.0, 2.0, 3.0}),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_value_in_iterable(self, _nam: str, _vals: Any) -> None:
        _val = list(_vals)[0]
        assert is_value_in_iterable(_val, _vals)
        assert is_in(_val, _vals)
        assert_value_in_iterable(_val, _vals)
        assert_in(_val, _vals)

    @parameterized.expand(
        (
            ("list", ["a", "b", "c"]),
            ("tuple", (1, 2, 3)),
            ("set", {1.0, 2.0, 3.0}),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_all_values_in_iterable(self, _nam: str, _vals: Any) -> None:
        _val = list(_vals)[0:2]
        assert is_all_values_in_iterable(_val, _vals)
        assert is_all_in(_val, _vals)
        assert_all_values_in_iterable(_val, _vals)
        assert_all_in(_val, _vals)

    @parameterized.expand(
        (
            ("list", ["a", "b", "c"]),
            ("tuple", (1, 2, 3)),
            ("set", {1.0, 2.0, 3.0}),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_any_values_in_iterable(self, _nam: str, _vals: Any) -> None:
        _val = list(_vals)[0:2] + ["z"]
        assert is_any_values_in_iterable(_val, _vals)
        assert is_any_in(_val, _vals)
        assert_any_values_in_iterable(_val, _vals)
        assert_any_in(_val, _vals)

    def test_raises_assert_value_of_type(self) -> None:
        with pytest.raises(TypeError):
            assert_value_of_type(5, str)
            assert_value_of_type("5", int)

    def test_raises_all_values_of_type(self) -> None:
        with pytest.raises(TypeError):
            assert_all_values_of_type((1, 2, 3, 4, 5), str)
            assert_all_values_of_type(("1", "2", "3", "4", "5"), int)

    def test_raises_assert_value_in_iterable(self) -> None:
        with pytest.raises(LookupError):
            assert_value_in_iterable("a", (1, 2, 3))
            assert_value_in_iterable(1, ("a", "b", "c"))

    def test_raises_assert_any_values_in_iterable(self) -> None:
        with pytest.raises(LookupError):
            assert_any_values_in_iterable(("a", "b"), (1, 2, 3))
            assert_any_values_in_iterable((1, 2), ("a", "b", "c"))

    def test_raises_assert_all_values_in_iterable(self) -> None:
        with pytest.raises(LookupError):
            assert_all_values_in_iterable(("a", "d"), ("a", "b", "c"))


## --------------------------------------------------------------------------- #
##  Contains                                                                ####
## --------------------------------------------------------------------------- #


class TestContains(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        values: tuple[str, ...] = ("key_SYSTEM", "key_CLUSTER", "key_GROUP", "key_NODE")
        cls.list_values = list(values)
        cls.tuple_values = tuple(values)
        cls.set_values = set(values)
        cls.values: dict[str, Union[list, tuple, set]] = {
            "list": cls.list_values,
            "tuple": cls.tuple_values,
            "set": cls.set_values,
        }

    @parameterized.expand(
        input=(
            ("list", "CLUSTER", True),
            ("tuple", "CLUSTER", True),
            ("set", "CLUSTER", True),
            ("list", "cluster", False),
            ("tuple", "nothing", False),
            ("set", "KEY", False),
        ),
        name_func=name_func_nested_list,
    )
    def test_any_element_contains(self, _typ: str, _val: str, _exp: bool) -> None:
        assert any_element_contains(self.values[_typ], _val) == _exp

    @parameterized.expand(
        input=(
            ("list", "key", True),
            ("tuple", "key", True),
            ("set", "key", True),
            ("list", "cluster", False),
            ("tuple", "nothing", False),
            ("set", "KEY", False),
        ),
        name_func=name_func_nested_list,
    )
    def test_all_elements_contains(self, _typ: str, _val: str, _exp: bool) -> None:
        assert all_elements_contains(self.values[_typ], _val) == _exp

    @parameterized.expand(
        input=(
            ("list", "key", "tuple_values"),
            ("tuple", "key", "tuple_values"),
            ("set", "key", "tuple_values"),
            ("list", "cluster", tuple()),
            ("tuple", "nothing", tuple()),
            ("set", "KEY", tuple()),
            ("tuple", "C", ("key_CLUSTER",)),
            ("tuple", "O", ("key_GROUP", "key_NODE")),
            ("tuple", "E", ("key_SYSTEM", "key_CLUSTER", "key_NODE")),
        ),
        name_func=name_func_nested_list,
    )
    def test_get_elements_containing(
        self, _typ: str, _val: str, _exp: str_tuple
    ) -> None:
        if _exp == "tuple_values":
            _exp = self.tuple_values
        _out: str_tuple = get_elements_containing(self.values[_typ], _val)
        if _typ == "set" and _val == "key":
            _out = tuple(sorted(_out))
            _exp = tuple(sorted(_exp))
        assert _out == _exp
