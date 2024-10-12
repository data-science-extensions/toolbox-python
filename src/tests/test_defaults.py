# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from unittest import TestCase

# ## Python Third Party Imports ----
import pytest
from parameterized import parameterized

# ## Local First Party Imports ----
from tests.setup import name_func_nested_list
from toolbox_python.defaults import defaults


# ---------------------------------------------------------------------------- #
#  Constants                                                                ####
# ---------------------------------------------------------------------------- #


TYPES: list[type] = [bool, int, str, float]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestDefaults(TestCase):

    def setUp(self) -> None:
        pass

    def test_defaults_basic_string(self) -> None:
        _input = "this"
        _output = defaults(value=_input)
        _expected = "this"
        assert _output == _expected

    def test_defaults_with_none(self) -> None:
        _input = "that"
        _output = defaults(value=None, default=_input)
        _expected = "that"
        assert _output == _expected

    @parameterized.expand(
        input=zip(TYPES, ["True", "1", 1, "1"]),
        name_func=name_func_nested_list,
    )
    def test_defaults_cast_types(self, cast_type, cast_value) -> None:
        _input = cast_value
        _output = defaults(value=_input, cast=cast_type)
        _expected = cast_type(_input)
        assert _output == _expected

    @parameterized.expand(
        input=zip(TYPES, ["True", "1", 1, "1"]),
        name_func=name_func_nested_list,
    )
    def test_defaults_cast_strings(self, cast_type, cast_value) -> None:
        _input = cast_value
        _expected = cast_type(_input)
        _output = defaults(value=_input, cast=str(cast_type.__name__))
        assert _output == _expected

    def test_defaults_invalid_cast(self) -> None:
        with pytest.raises(AttributeError):
            defaults(value="next", cast="bad_type")

    def test_defaults_all_blank(self) -> None:
        with pytest.raises(AttributeError):
            defaults(value=None, default=None)
