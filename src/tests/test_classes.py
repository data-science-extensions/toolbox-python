# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from random import Random
from unittest import TestCase

# ## Local First Party Imports ----
from toolbox_python.classes import get_full_class_name
from toolbox_python.defaults import Defaults


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestStrings(TestCase):

    def setUp(self) -> None:
        pass

    def test_get_full_class_name_1(self) -> None:
        _input = Defaults()
        _output: str = get_full_class_name(_input)
        _expected = "toolbox_python.defaults.Defaults"
        assert _output == _expected

    def test_get_full_class_name_2(self) -> None:
        _input = "str"
        _output: str = get_full_class_name(_input)
        _expected = "str"
        assert _output == _expected

    def test_get_full_class_name_3(self) -> None:
        _input = Random()
        _output: str = get_full_class_name(_input)
        _expected = "random.Random"
        assert _output == _expected
