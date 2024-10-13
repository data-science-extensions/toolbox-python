# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import logging
from typing import Union
from unittest import TestCase

# ## Python Third Party Imports ----
import pytest
import requests
from typeguard import TypeCheckError

# ## Local First Party Imports ----
from toolbox_python.collection_types import str_list
from toolbox_python.output import list_columns, print_or_log_output


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestPrintOrLogOutput(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.message = "Message for:"
        cls.log: logging.Logger = logging.getLogger(__name__)

    @pytest.fixture(autouse=True)
    def _pass_fixtures(
        self, capsys: pytest.CaptureFixture, caplog: pytest.LogCaptureFixture
    ) -> None:
        self.capsys: pytest.CaptureFixture = capsys
        self.caplog: pytest.LogCaptureFixture = caplog
        self.caplog.set_level("notset".upper())

    def test_print_output(self) -> None:
        print_or_log_output(
            message=f"{self.message} print",
            print_or_log="print",
        )
        captured: str = self.capsys.readouterr().out
        assert captured == "Message for: print\n"

    def test_log_info_output(self) -> None:
        print_or_log_output(
            message=f"{self.message} info",
            print_or_log="log",
            log=self.log,
            log_level="info",
        )
        assert self.caplog.records[0].levelname == "info".upper()
        assert self.caplog.records[0].message == "Message for: info"
        self.caplog.clear()

    def test_log_debug_output(self) -> None:
        print_or_log_output(
            message=f"{self.message} debug",
            print_or_log="log",
            log=self.log,
            log_level="debug",
        )
        assert self.caplog.records[0].levelname == "debug".upper()
        assert self.caplog.records[0].message == "Message for: debug"
        self.caplog.clear()

    def test_log_warning_output(self) -> None:
        print_or_log_output(
            message=f"{self.message} warning",
            print_or_log="log",
            log=self.log,
            log_level="warning",
        )
        assert self.caplog.records[0].levelname == "warning".upper()
        assert self.caplog.records[0].message == "Message for: warning"
        self.caplog.clear()

    def test_log_error_output(self) -> None:
        print_or_log_output(
            message=f"{self.message} error",
            print_or_log="log",
            log=self.log,
            log_level="error",
        )
        assert self.caplog.records[0].levelname == "error".upper()
        assert self.caplog.records[0].message == "Message for: error"
        self.caplog.clear()

    def test_log_critical_output(self) -> None:
        print_or_log_output(
            message=f"{self.message} critical",
            print_or_log="log",
            log=self.log,
            log_level="critical",
        )
        assert self.caplog.records[0].levelname == "critical".upper()
        assert self.caplog.records[0].message == "Message for: critical"
        self.caplog.clear()

    def test_none_output(self) -> None:
        result: None = print_or_log_output("Test `None`", print_or_log=None)
        assert result is None

    def test_raises_type_error(self) -> None:
        with pytest.raises(TypeError):
            print_or_log_output(
                message=f"{self.message} error",
                print_or_log="log",
                log=None,
                log_level=None,
            )

    def test_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            print_or_log_output(
                message=f"{self.message} error",
                print_or_log="log",
                log=self.log,
                log_level=None,
            )

    def test_invalid_input_01(self) -> None:
        with pytest.raises(TypeCheckError):
            print_or_log_output(
                message=1,
                print_or_log="log",
                log=self.log,
                log_level="info",
            )

    def test_invalid_input_02(self) -> None:
        with pytest.raises(TypeCheckError):
            print_or_log_output(
                message=self.message,
                print_or_log="invalid",
                log=self.log,
                log_level="info",
            )

    def test_invalid_input_03(self) -> None:
        with pytest.raises(TypeCheckError):
            print_or_log_output(
                message=self.message,
                print_or_log="log",
                log="invalid",
                log_level="info",
            )

    def test_invalid_input_04(self) -> None:
        with pytest.raises(TypeCheckError):
            print_or_log_output(
                message=self.message,
                print_or_log="log",
                log=self.log,
                log_level="invalid",
            )


class TestListColumnsOutput(TestCase):

    def setUp(self) -> None:
        pass

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys: pytest.CaptureFixture) -> None:
        self.capsys: pytest.CaptureFixture = capsys

    @staticmethod
    def get_list_of_words(num_words: int = 100) -> str_list:
        word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
        response: requests.Response = requests.get(word_url)
        words: str_list = response.content.decode().splitlines()
        return words[:num_words]

    def test_1(self) -> None:
        output: Union[str, None] = list_columns(
            self.get_list_of_words(4 * 5),
            print_output=False,
        )

        expected: str = "\n".join(
            [
                "a             abandoned     able          abraham       ",
                "aa            abc           aboriginal    abroad        ",
                "aaa           aberdeen      abortion      abs           ",
                "aaron         abilities     about         absence       ",
                "ab            ability       above         absent        ",
            ]
        )
        assert output == expected

    def test_2(self) -> None:
        output: Union[str, None] = list_columns(
            self.get_list_of_words(3),
            print_output=False,
        )
        expected = """a      aa     aaa    """
        assert output == expected

    def test_3(self) -> None:
        output: Union[str, None] = list_columns(
            self.get_list_of_words(5),
            cols_wide=2,
            columnwise=True,
            print_output=False,
        )
        expected: str = "\n".join(
            [
                "a        aaron    ",
                "aa       ab       ",
                "aaa               ",
            ]
        )
        assert output == expected

    def test_4(self) -> None:
        list_columns(
            self.get_list_of_words(4 * 3),
            columnwise=False,
            cols_wide=4,
            print_output=True,
        )
        output: str_list = self.capsys.readouterr().out.split("\n")
        expected: str_list = [
            "a             aa            aaa           aaron         ",
            "ab            abandoned     abc           aberdeen      ",
            "abilities     ability       able          aboriginal    ",
            "",
        ]
        assert output == expected
