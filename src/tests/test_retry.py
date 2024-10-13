# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from pprint import pprint
from unittest import TestCase

# ## Python Third Party Imports ----
import pytest

# ## Local First Party Imports ----
from toolbox_python.retry import retry


# ---------------------------------------------------------------------------- #
#  Custom Errors                                                            ####
# ---------------------------------------------------------------------------- #


class ExpectedError(RuntimeError):
    pass


class UnexpectedError(RuntimeError):
    pass


class UnknownError(RuntimeError):
    pass


class UnexpectedKnownError(RuntimeError):
    pass


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestRetryDecorator(TestCase):
    def setUp(self) -> None:
        pass

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys, caplog) -> None:
        self.capsys: pytest.CaptureFixture = capsys
        self.caplog: pytest.LogCaptureFixture = caplog
        self.caplog.set_level("notset".upper())

    @staticmethod
    def error_function() -> None:
        raise ExpectedError("Immediate error raised")

    @retry(exceptions=ExpectedError, tries=5, delay=1, print_or_log="print")
    def fail_always_print(self) -> None:
        return self.error_function()

    def test_fail_always_print(self) -> None:
        """
        - Will retry the same function 5 times.
        - Each time, the function will throw the `ExpectedError`; which it is expecting to see, and will thus re-try again.
        - After 5 iterations, it will throw the `RuntimeError` because it couldn't execute successfully after 5 iterations.
        """
        with self.assertRaises(RuntimeError) as e:
            self.fail_always_print()
        console_print = self.capsys.readouterr()
        error_output = "Still could not write after 5 iterations. Please check."
        error_string = "Caught an expected error at iteration {i}: `{__name__}`. Retrying in 1 seconds..."
        error_message = "\n".join(
            [
                error_string.format(i=i, __name__=f"{__name__}.ExpectedError")
                for i in range(1, 6)
            ]
        )
        error_message += f"\n{error_output}\n"
        assert str(e.exception) == error_output
        assert console_print.out == error_message

    @retry(exceptions=ExpectedError, tries=5, delay=1, print_or_log="log")
    def fail_always_log(self) -> None:
        return self.error_function()

    def test_fail_always_log(self) -> None:
        """
        - Same as `test_print_fail_always()`, but to test the `log` output
        """
        with self.assertRaises(RuntimeError) as e:
            self.fail_always_log()
        log_records = self.caplog.records
        error_output = "Still could not write after 5 iterations. Please check."
        error_string = "Caught an expected error at iteration {i}: `{__name__}`. Retrying in 1 seconds..."
        assert str(e.exception) == error_output
        for index, record in enumerate(log_records):
            if index < 5:
                assert record.levelname == "warning".upper()
                assert record.message == error_string.format(
                    i=index + 1, __name__=f"{__name__}.ExpectedError"
                )
            else:
                assert record.levelname == "error".upper()
                assert record.message == error_output

    @retry(exceptions=UnknownError, tries=3, delay=1, print_or_log="print")
    def fail_unknown_print(self):
        return self.error_function()

    def test_fail_first_print(self) -> None:
        """
        - Will retry the same function 5 times.
        - During the first time, it will see an error that it is not expecting: `UnexpectedError`.
        - At this point, it will fail and return.
        """
        with self.assertRaises(RuntimeError) as e:
            self.fail_unknown_print()
        console_print = self.capsys.readouterr()
        error_output = (
            f"Caught an unexpected error at iteration 1: `{__name__}.ExpectedError`."
        )
        assert console_print.out == error_output + "\n"
        assert str(e.exception) == error_output

    @retry(exceptions=UnknownError, tries=3, delay=1, print_or_log="log")
    def fail_unknown_log(self):
        return self.error_function()

    def test_fail_first_log(self) -> None:
        """
        - Same as `test_print_fail_first()`, but test `log` output.
        """
        with self.assertRaises(RuntimeError) as e:
            self.fail_unknown_log()
        log_records = self.caplog.records
        error_output = (
            f"Caught an unexpected error at iteration 1: `{__name__}.ExpectedError`."
        )
        pprint(log_records)
        assert log_records[0].levelname == "error".upper()
        assert log_records[0].message == error_output
        assert str(e.exception) == error_output

    def error_after_n(self, iterations: int = 3) -> None:
        self.iteration += 1
        if self.iteration <= iterations:
            raise ExpectedError("Expected Error.")
        else:
            raise UnexpectedError("Unexpected Error.")

    @retry(exceptions=ExpectedError, tries=5, delay=1, print_or_log="print")
    def fail_after_n_print(self, iterations: int = 3) -> None:
        return self.error_after_n(iterations=iterations)

    def test_fail_after_n_print(self) -> None:
        """
        - Will retry the same function 5 times.
        - During the first 3, it will receive an error that it is expecting to see: `ExpectedError`.
        - During the 4th iteration, it will receive: `UnexpectedError`.
        - At that point, it will return.
        """
        self.iteration = 0
        num_fail_iterations = 3
        with self.assertRaises(RuntimeError) as e:
            self.fail_after_n_print(iterations=num_fail_iterations)
        console_print = self.capsys.readouterr()
        error_output = f"Caught an unexpected error at iteration {num_fail_iterations+1}: `tests.test_retry.UnexpectedError`."
        error_string = "Caught an expected error at iteration {i}: `{__name__}`. Retrying in 1 seconds..."
        error_message = "\n".join(
            [
                error_string.format(i=i, __name__=f"{__name__}.ExpectedError")
                for i in range(1, num_fail_iterations + 1)
            ]
        )
        error_message += f"\n{error_output}\n"
        assert str(e.exception) == error_output
        assert console_print.out == error_message

    @retry(exceptions=ExpectedError, tries=5, delay=1, print_or_log="log")
    def fail_after_n_log(self, iterations: int = 3) -> None:
        return self.error_after_n(iterations=iterations)

    def test_fail_after_n_log(self) -> None:
        """
        - Same as `test_fail_after_n_print()`, but for `log`.
        """
        self.iteration = 0
        num_fail_iterations = 3
        with self.assertRaises(RuntimeError) as e:
            self.fail_after_n_log(iterations=num_fail_iterations)
        log_records = self.caplog.records
        error_output = f"Caught an unexpected error at iteration {num_fail_iterations+1}: `tests.test_retry.UnexpectedError`."
        error_string = "Caught an expected error at iteration {i}: `{__name__}`. Retrying in 1 seconds..."
        for index, record in enumerate(log_records):
            if index < num_fail_iterations:
                assert record.levelname == "warning".upper()
                assert record.message == error_string.format(
                    i=index + 1, __name__=f"{__name__}.ExpectedError"
                )
            else:
                assert record.levelname == "error".upper()
                assert record.message == error_output
        assert str(e.exception) == error_output

    @staticmethod
    def pass_function() -> None:
        return None

    @retry(tries=5, delay=1, print_or_log="print")
    def succeed_print(self) -> None:
        return self.pass_function()

    def test_succeed_print(self) -> None:
        """
        - Will not cause any errors
        """
        result = self.succeed_print()
        console_print = self.capsys.readouterr()
        self.assertIsNone(result)
        assert console_print.out == "Successfully executed at iteration 1.\n"

    @retry(tries=5, delay=1, print_or_log="log")
    def succeed_log(self) -> None:
        return self.pass_function()

    def test_succeed_log(self) -> None:
        """
        - Same as `test_no_fail_print()`, but for `log`.
        """
        result = self.succeed_log()
        log_records = self.caplog.records
        self.assertIsNone(result)
        assert log_records[0].levelname == "info".upper()
        assert log_records[0].message == "Successfully executed at iteration 1."

    def pass_after_n(self, iterations: int = 3):
        self.iteration += 1
        if self.iteration <= iterations:
            raise ExpectedError("Expected Error.")
        else:
            return None

    @retry(exceptions=ExpectedError, tries=5, delay=1, print_or_log="print")
    def succeed_after_n_print(self, iterations: int = 3) -> None:
        return self.pass_after_n(iterations=iterations)

    def test_succeed_after_n_print(self) -> None:
        self.iteration = 0
        num_fail_iterations = 3
        result = self.succeed_after_n_print(iterations=num_fail_iterations)
        console_print = self.capsys.readouterr()
        output = f"Successfully executed at iteration {num_fail_iterations+1}."
        error_string = "Caught an expected error at iteration {i}: `{__name__}`. Retrying in 1 seconds..."
        error_message = "\n".join(
            [
                error_string.format(i=i, __name__=f"{__name__}.ExpectedError")
                for i in range(1, num_fail_iterations + 1)
            ]
        )
        error_message += f"\n{output}\n"
        self.assertIsNone(result)
        assert console_print.out == error_message

    @retry(exceptions=ExpectedError, tries=5, delay=1, print_or_log="log")
    def succeed_after_n_log(self, iterations: int = 3) -> None:
        return self.pass_after_n(iterations=iterations)

    def test_succeed_after_n_log(self) -> None:
        self.iteration = 0
        num_fail_iterations = 3
        result = self.succeed_after_n_log(iterations=num_fail_iterations)
        log_records = self.caplog.records
        output = f"Successfully executed at iteration {num_fail_iterations+1}."
        error_string = "Caught an expected error at iteration {i}: `{__name__}`. Retrying in 1 seconds..."
        self.assertIsNone(result)
        for index, record in enumerate(log_records):
            if index < num_fail_iterations:
                assert record.levelname == "warning".upper()
                assert record.message == error_string.format(
                    i=index + 1, __name__=f"{__name__}.ExpectedError"
                )
            else:
                assert record.levelname == "info".upper()
                assert record.message == output

    def test_fail_invalid_tries(self) -> None:
        with self.assertRaises(ValueError):

            @retry(tries=-2)
            def fail_invalid_tries() -> None:
                return self.pass_function()

            fail_invalid_tries()

    def test_fail_invalid_delay(self) -> None:
        with self.assertRaises(ValueError):

            @retry(delay=-2)
            def fail_invalid_delay() -> None:
                return self.pass_function()

            fail_invalid_delay()

    @staticmethod
    def throw_unexpected_known_error(known_error: type = ValueError) -> None:
        raise UnexpectedKnownError(
            f"Throwing UnexpectedError. "
            f"Containing known Exception: {known_error.__name__}"
        )

    @retry(exceptions=ValueError, tries=5, delay=0, print_or_log="print")
    def succeed_unexpected_known_error(self, known_error: type = ValueError) -> None:
        return self.throw_unexpected_known_error(known_error=known_error)

    @retry(exceptions=ValueError, tries=5, delay=0, print_or_log="print")
    def fail_unexpected_known_error(self, unknown_error: type = ReferenceError) -> None:
        return self.throw_unexpected_known_error(known_error=unknown_error)

    def test_succeed_print_with_hidden_exception(self) -> None:
        with self.assertRaises(RuntimeError):
            _ = self.succeed_unexpected_known_error(known_error=ValueError)
        console_print = self.capsys.readouterr()
        num_iterations = 5
        output = (
            f"Still could not write after {num_iterations} iterations. Please check."
        )
        error_string = (
            "Caught an unexpected, known error at iteration {i}: `{__name__}`.\n"
            "Who's message contains reference to underlying exception(s): ['ValueError'].\n"
            "Retrying in 0 seconds..."
        )
        error_message = "\n".join(
            [
                error_string.format(i=i, __name__=f"{__name__}.UnexpectedKnownError")
                for i in range(1, num_iterations + 1)
            ]
        )
        error_message += f"\n{output}\n"
        assert console_print.out == error_message

    def test_fail_print_with_hidden_exception(self) -> None:
        with self.assertRaises(RuntimeError):
            _ = self.fail_unexpected_known_error(unknown_error=ReferenceError)
        console_print = self.capsys.readouterr()
        error_message = "Caught an unexpected error at iteration 1: `tests.test_retry.UnexpectedKnownError`."
