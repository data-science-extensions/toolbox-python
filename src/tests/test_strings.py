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

# ## Local First Party Imports ----
from toolbox_python.collection_types import str_list
from toolbox_python.strings import (
    str_contains,
    str_contains_all,
    str_contains_any,
    str_replace,
    str_separate_number_chars,
)


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestStrings(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.long_string = "This long string"
        cls.complex_sentence = "Because my pizza was cold, I put it in the microwave."

    def test_str_replace_1(self) -> None:
        _input: str = self.long_string
        _output: str = str_replace(_input, " ", "_")
        _expected: str = self.long_string.replace(" ", "_")
        assert _output == _expected

    def test_str_replace_2(self) -> None:
        _input: str = self.complex_sentence
        _output: str = str_replace(_input)
        _expected: str = (
            self.complex_sentence.replace(" ", "").replace(",", "").replace(".", "")
        )
        assert _output == _expected

    def test_str_contains_valid(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains(_input, "long")
        _expected = True
        assert _output == _expected

    def test_str_contains_invalid(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains(_input, "short")
        _expected = False
        assert _output == _expected

    def test_str_contains_any_valid(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains_any(_input, ["long", "short"])
        _expected = True
        assert _output == _expected

    def test_str_contains_any_invalid(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains_any(_input, ["this", "that"])
        _expected = False
        assert _output == _expected

    def test_str_contains_all_valid(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains_all(_input, ["long", "string"])
        _expected = True
        assert _output == _expected

    def test_str_contains_all_some(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains_all(_input, ["long", "something"])
        _expected = False
        assert _output == _expected

    def test_str_contains_all_none(self) -> None:
        _input: str = self.long_string
        _output: bool = str_contains_all(_input, ["this", "that"])
        _expected = False
        assert _output == _expected


class TestNumberCharacterSeparation(TestCase):

    def setUp(self) -> None:
        pass

    def test_str_separate_number_chars1(self) -> None:
        _input = "-12.1grams"
        _output: str_list = str_separate_number_chars(_input)
        _expected: str_list = ["-12.1", "grams"]
        assert _output == _expected

    def test_str_separate_number_chars2(self) -> None:
        _input = "abcd2343 abw34324 abc3243-23A 123"
        _output: str_list = str_separate_number_chars(_input)
        _expected: str_list = [
            "abcd",
            "2343",
            "abw",
            "34324",
            "abc",
            "3243",
            "-23",
            "A",
            "123",
        ]
        assert _output == _expected
