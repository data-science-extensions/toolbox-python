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

# ## Local First Party Imports ----
from toolbox_python.bools import strtobool


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestBools(TestCase):
    def setUp(self) -> None:
        pass

    def test_strtobool_1(self) -> None:
        _input = "true"
        _output: bool = strtobool(_input)
        _expected = True
        assert _output == _expected

    def test_strtobool_2(self) -> None:
        _input = "t"
        _output: bool = strtobool(_input)
        _expected = True
        assert _output == _expected

    def test_strtobool_3(self) -> None:
        _input = "false"
        _output: bool = strtobool(_input)
        _expected = False
        assert _output == _expected

    def test_strtobool_4(self) -> None:
        _input = "f"
        _output: bool = strtobool(_input)
        _expected = False
        assert _output == _expected

    def test_strtobool_5(self) -> None:
        _input = 5
        with pytest.raises((ValueError, KeyError)):
            _output: bool = strtobool(_input)
