# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from typing import Any
from unittest import TestCase

# ## Python Third Party Imports ----
import pytest
from parameterized import parameterized

# ## Local First Party Imports ----
from tests.setup import name_func_predefined_name
from toolbox_python.checkers import (
    assert_all_in,
    assert_all_type,
    assert_all_values_in_iterable,
    assert_all_values_of_type,
    assert_any_in,
    assert_any_values_in_iterable,
    assert_in,
    assert_type,
    assert_value_in_iterable,
    assert_value_of_type,
    is_all_in,
    is_all_type,
    is_all_values_in_iterable,
    is_all_values_of_type,
    is_any_in,
    is_any_values_in_iterable,
    is_in,
    is_type,
    is_value_in_iterable,
    is_value_of_type,
)


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
            ("str", "a"),
            ("int", 1),
            ("float", 2.5),
            ("bool", True),
            ("tuple", (1, 2)),
            ("list", ["a", "a"]),
            ("set", {1.0, 1.0}),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_value_of_type(self, _nam: str, _val: Any) -> None:
        _typ = eval(_nam)
        assert is_value_of_type(_val, _typ)
        assert is_type(_val, _typ)
        assert_type(_val, _typ)
        assert_value_of_type(_val, _typ)

    @parameterized.expand(
        (
            ("str", ("a", "b", "c")),
            ("int", (1, 2, 3)),
            ("float", (1.0, 2.0, 3.0)),
            ("bool", (True, False, True)),
            ("tuple", ((1, 2), (3, 4), (5, 6))),
            ("list", (["a", "b"], ["c", "d"], ["e", "f"])),
            ("set", ({1.0, 2.0}, {3.0, 4.0}, {5.0, 6.0})),
        ),
        name_func=name_func_predefined_name,
    )
    def test_is_all_values_of_type(self, _nam: str, _vals: Any) -> None:
        _typ = eval(_nam)
        assert is_all_values_of_type(_vals, _typ)
        assert is_all_type(_vals, _typ)
        assert_all_values_of_type(_vals, _typ)
        assert_all_type(_vals, _typ)

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
##  Major Objects                                                           ####
## --------------------------------------------------------------------------- #


### Comment ----
...
