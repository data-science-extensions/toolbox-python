# ============================================================================ #
#                                                                              #
#     Title   : Retry                                                          #
#     Purpose : Automatically retry a given function when a specific           #
#               `Exception` is thrown.                                         #
#                                                                              #
# ============================================================================ #


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Overview                                                              ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Description                                                              ####
# ---------------------------------------------------------------------------- #


"""
!!! note "Summary"
    The `retry` module is for enabling automatic retrying of a given function when a specific `Exception` is thrown.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
import inspect
import logging
from builtins import Exception
from functools import wraps
from logging import Logger
from time import sleep
from types import ModuleType
from typing import Any, Callable, Literal, NoReturn, Optional, TypeVar, Union, overload

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.checkers import assert_is_valid
from toolbox_python.classes import get_full_class_name
from toolbox_python.collection_types import str_list
from toolbox_python.output import print_or_log_output


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #


__all__: str_list = ["retry"]


# ---------------------------------------------------------------------------- #
#  Types                                                                    ####
# ---------------------------------------------------------------------------- #


_exceptions = Union[
    type[Exception],
    list[type[Exception]],
    tuple[type[Exception], ...],
]
"""
!!! note "Summary"
    This
"""


R = TypeVar("R")


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Classes                                                               ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class _Retry:
    """
    !!! note "Summary"
        A helper class to handle the retry logic for the `retry` decorator.

    ???+ abstract "Details"
        This class is not intended to be used directly. Instead, it is used internally by the `retry` decorator to manage the retry logic.

    Methods:
        run(): Run the retry loop for the given function.
    """

    def __init__(
        self,
        exceptions: _exceptions,
        tries: int,
        delay: int,
        print_or_log: Literal["print", "log"],
        log: Optional[Logger],
    ) -> None:
        """
        !!! note "Summary"
            Initialize the `_Retry` class with the given parameters.

        Params:
            exceptions (_exceptions):
                A given single or collection of expected exceptions for which to catch and retry for.
            tries (int):
                The number of retries to attempt.
            delay (int):
                The number of seconds to delay between each retry.
            print_or_log (Literal["print", "log"]):
                Whether or not the messages should be written to the terminal in a `#!py print()` statement, or to a log file in a `#!py log()` statement.
            log (Optional[Logger]):
                An optional logger instance to use when `print_or_log` is set to `"log"`.
        """
        self.exceptions: tuple[type[Exception], ...] = (
            tuple(exceptions) if isinstance(exceptions, (list, tuple)) else (exceptions,)
        )
        self.tries: int = tries
        self.delay: int = delay
        self.print_or_log: Literal["print", "log"] = print_or_log
        self.log: Optional[Logger] = log

    def run(self, func: Callable[..., R], *args: Any, **kwargs: Any) -> R:
        """
        !!! note "Summary"
            Run the retry loop for the given function.
        """
        for i in range(1, self.tries + 1):
            try:
                results = func(*args, **kwargs)
                self._handle_success(i)
                return results
            except self.exceptions as e:
                self._handle_expected_error(i, e)
            except Exception as exc:
                self._handle_unexpected_error(i, exc)
        self._handle_final_failure()

    def _handle_success(self, i: int) -> None:
        message: str = f"Successfully executed at iteration {i}."
        print_or_log_output(
            message=message,
            print_or_log=self.print_or_log,
            log=self.log,
            log_level="info",
        )

    def _handle_expected_error(self, i: int, e: Exception) -> None:
        message = (
            f"Caught an expected error at iteration {i}: "
            f"`{get_full_class_name(e)}`. "
            f"Retrying in {self.delay} seconds..."
        )
        print_or_log_output(
            message=message,
            print_or_log=self.print_or_log,
            log=self.log,
            log_level="warning",
        )
        sleep(self.delay)

    def _handle_unexpected_error(self, i: int, exc: Exception) -> None:
        excs = self.exceptions if isinstance(self.exceptions, (list, tuple)) else (self.exceptions,)
        exc_names: list[str] = [e.__name__ for e in excs]
        if any(name in f"{exc}" for name in exc_names):
            caught_errors: list[str] = [name for name in exc_names if name in f"{exc}"]
            message: str = (
                f"Caught an unexpected, known error at iteration {i}: "
                f"`{get_full_class_name(exc)}`.\n"
                f"Who's message contains reference to underlying exception(s): {caught_errors}.\n"
                f"Retrying in {self.delay} seconds..."
            )
            print_or_log_output(
                message=message,
                print_or_log=self.print_or_log,
                log=self.log,
                log_level="warning",
            )
            sleep(self.delay)
        else:
            message = f"Caught an unexpected error at iteration {i}: `{get_full_class_name(exc)}`."
            print_or_log_output(
                message=message,
                print_or_log=self.print_or_log,
                log=self.log,
                log_level="error",
            )
            raise RuntimeError(message) from exc

    def _handle_final_failure(self) -> NoReturn:
        message: str = f"Still could not write after {self.tries} iterations. Please check."
        print_or_log_output(
            message=message,
            print_or_log=self.print_or_log,
            log=self.log,
            log_level="error",
        )
        raise RuntimeError(message)


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@overload
@typechecked
def retry(
    exceptions: _exceptions = Exception,
    tries: int = 1,
    delay: int = 0,
    print_or_log: Literal["print"] = "print",
) -> Callable[[Callable[..., R]], Callable[..., R]]: ...
@overload
@typechecked
def retry(
    exceptions: _exceptions = Exception,
    tries: int = 1,
    delay: int = 0,
    print_or_log: Literal["log"] = "log",
) -> Callable[[Callable[..., R]], Callable[..., R]]: ...
@typechecked
def retry(
    exceptions: _exceptions = Exception,
    tries: int = 1,
    delay: int = 0,
    print_or_log: Literal["print", "log"] = "print",
) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """
    !!! note "Summary"
        Retry a given function a number of times. Catching any known exceptions when they are given. And returning any output to either a terminal or a log file.

    !!! deprecation "Deprecated"
        This function is deprecated. Please use the [`retry()`][func] decorator from the [`stamina`][docs] package instead.<br>
        For more info, see: [Docs][docs], [GitHub][github], [PyPi][pypi].
        [func]: https://stamina.hynek.me/en/stable/api.html#stamina.retry
        [docs]: https://stamina.hynek.me/en/stable/index.html
        [github]: https://github.com/hynek/stamina/
        [pypi]: https://pypi.org/project/stamina/

    ???+ abstract "Details"
        This function should always be implemented as a decorator.<br>
        It is written based on the premise that a certain process may fail and return a given message, but that is known and expected, and you just want to wait a second or so then retry again.<br>
        Typically, this is seen in async processes, or when writing data to a `delta` table when there may be concurrent read/writes occurring at the same time. In these instances, you will know the error message and can re-try again a certain number of times.

    Params:
        exceptions (_exceptions, optional):
            A given single or collection of expected exceptions for which to catch and retry for.<br>
            Defaults to `#!py Exception`.
        tries (int, optional):
            The number of retries to attempt. If the underlying process is still failing after this number of attempts, then throw a hard error and alert the user.<br>
            Defaults to `#!py 1`.
        delay (int, optional):
            The number of seconds to delay between each retry.<br>
            Defaults to `#!py 0`.
        print_or_log (Literal["print", "log"], optional):
            Whether or not the messages should be written to the terminal in a `#!py print()` statement, or to a log file in a `#!py log()` statement.<br>
            Defaults to `#!py "print"`.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        (ValueError):
            If either `tries` or `delay` are less than `#!py 0`
        (RuntimeError):
            If _either_ an unexpected `#!py Exception` was thrown, which was not declared in the `exceptions` collection, _or_ if the `func` was still not able to be executed after `tries` number of iterations.

    Returns:
        result (Optional[Any]):
            The result from the underlying function, if any.

    ???+ example "Examples"

        ```pycon {.py .python linenums="1" title="Imports"}
        >>> from toolbox_python.retry import retry
        ```

        ```{.py .python linenums="1" title="Example 1: No error"}
        >>> @retry(tries=5, delay=1, print_or_log="print")
        >>> def simple_func(var1: str = "this") -> str:
        ...     return var1
        ...
        >>> simple_func()
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        # No error
        ```
        </div>

        ```{.py .python linenums="1" title="Example 2: Expected error"}
        >>> @retry(exceptions=TypeError, tries=5, delay=1, print_or_log="print")
        >>> def failing_func(var1: str = "that") -> None:
        ...     raise ValueError("Incorrect value")
        ...
        >>> failing_func()
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        Caught an expected error at iteration 1: `ValueError`. Retrying in 1 seconds...
        Caught an expected error at iteration 2: `ValueError`. Retrying in 1 seconds...
        Caught an expected error at iteration 3: `ValueError`. Retrying in 1 seconds...
        Caught an expected error at iteration 4: `ValueError`. Retrying in 1 seconds...
        Caught an expected error at iteration 5: `ValueError`. Retrying in 1 seconds...
        RuntimeError: Still could not write after 5 iterations. Please check.
        ```
        </div>

    ??? success "Credit"
        Inspiration from:

        - https://pypi.org/project/retry/
        - https://stackoverflow.com/questions/21786382/pythonic-way-of-retry-running-a-function#answer-21788594
    """

    assert_is_valid(tries, ">=", 0)
    assert_is_valid(delay, ">=", 0)

    exceptions = tuple(exceptions) if isinstance(exceptions, (list, tuple)) else (exceptions,)

    log: Optional[Logger] = None

    if print_or_log == "log":
        stk: inspect.FrameInfo = inspect.stack()[2]
        mod: Union[ModuleType, None] = inspect.getmodule(stk[0])
        if mod is not None:
            log: Optional[Logger] = logging.getLogger(mod.__name__)

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            retry_handler = _Retry(
                exceptions=exceptions,
                tries=tries,
                delay=delay,
                print_or_log=print_or_log,
                log=log,
            )
            return retry_handler.run(func, *args, **kwargs)

        return wrapper

    return decorator
