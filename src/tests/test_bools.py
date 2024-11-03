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
from toolbox_python.bools import STR_TO_BOOL_MAP, strtobool


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestBools(TestCase):

    def setUp(self) -> None:
        pass

    @parameterized.expand(
        input=((_bool, _str) for _str, _bool in STR_TO_BOOL_MAP.items()),
        name_func=name_func_nested_list,
    )
    def test_strtobool(self, _expected: bool, _input: str) -> None:
        _output: bool = strtobool(_input)
        assert _output == _expected

    def test_strtobool_raises(self) -> None:
        _input = 5
        with pytest.raises(ValueError):
            _output: bool = strtobool(_input)
