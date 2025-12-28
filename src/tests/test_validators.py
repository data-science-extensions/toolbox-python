# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from unittest import TestCase

# ## Python Third Party Imports ----
from parameterized import parameterized
from pytest import raises

# ## Local First Party Imports ----
from tests.setup import name_func_predefined_name
from toolbox_python.validators import Validators


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestValidators(TestCase):

    def setUp(self) -> None:
        pass

    ## ----------------------------------------------------------------------- #
    ##  _value_is_between                                                   ####
    ## ----------------------------------------------------------------------- #

    @parameterized.expand(
        input=(
            ("within_range", 5, 0, 10, True),
            ("at_min", 0, 0, 10, True),
            ("at_max", 10, 0, 10, True),
            ("below_range", -1, 0, 10, False),
            ("above_range", 11, 0, 10, False),
            ("float_within", 5.5, 5.0, 6.0, True),
        ),
        name_func=name_func_predefined_name,
    )
    def test_value_is_between(self, _name, value, min_val, max_val, expected) -> None:
        assert Validators._value_is_between(value, min_val, max_val) == expected

    def test_value_is_between_raises(self) -> None:
        with raises(ValueError, match="Invalid range"):
            Validators._value_is_between(5, 10, 0)

    ## ----------------------------------------------------------------------- #
    ##  _assert_value_is_between                                            ####
    ## ----------------------------------------------------------------------- #

    def test_assert_value_is_between_valid(self) -> None:
        Validators._assert_value_is_between(5, 0, 10)

    def test_assert_value_is_between_invalid(self) -> None:
        with raises(AssertionError, match="Invalid Value"):
            Validators._assert_value_is_between(11, 0, 10)

    ## ----------------------------------------------------------------------- #
    ##  _all_values_are_between                                             ####
    ## ----------------------------------------------------------------------- #

    @parameterized.expand(
        input=(
            ("all_within", [1, 2, 3], 0, 5, True),
            ("one_below", [-1, 2, 3], 0, 5, False),
            ("one_above", [1, 2, 6], 0, 5, False),
            ("empty_list", [], 0, 5, True),
        ),
        name_func=name_func_predefined_name,
    )
    def test_all_values_are_between(self, _name, values, min_val, max_val, expected) -> None:
        assert Validators._all_values_are_between(values, min_val, max_val) == expected

    ## ----------------------------------------------------------------------- #
    ##  _assert_all_values_are_between                                      ####
    ## ----------------------------------------------------------------------- #

    def test_assert_all_values_are_between_valid(self) -> None:
        Validators._assert_all_values_are_between([1, 2, 3], 0, 5)

    def test_assert_all_values_are_between_invalid(self) -> None:
        with raises(AssertionError, match="Values not between"):
            Validators._assert_all_values_are_between([1, 6, -1], 0, 5)
