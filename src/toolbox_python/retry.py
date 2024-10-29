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
from typing import Any, Callable, Literal, Optional, Union

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
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


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Classes                                                               ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class Retry:
    pass


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def retry(
    exceptions: _exceptions = Exception,
    tries: int = 1,
    delay: int = 0,
    print_or_log: Optional[Literal["print", "log"]] = "print",
) -> Optional[Any]:
    """
    !!! note "Summary"
        Retry a given function a number of times. Catching any known exceptions when they are given. And retrurning any output to either a terminal or a log file.

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
        print_or_log (Optional[Literal["print", "log"]], optional):
            Whether or not the messages should be written to the terminal in a `#!py print()` statement, or to a log file in a `#!py log()` statement.<br>
            Defaults to `#!py "print"`.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        ValueError: If either `tries` or `delay` are less than `#!py 0`
        RuntimeError: If _either_ an unexpected `#!py Exception` was thrown, which was not declared in the `exceptions` collection, _or_ if the `func` was still not able to be executed after `tries` number of iterations.

    Returns:
        result (Optional[Any]):
            The result from the underlying function, if any.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Imports"}
        >>> from toolbox_python.retry import retry
        ```

        ```{.py .python linenums="1" title="Example 1: No error"}
        >>> @retry(tries=5, delay=1, print_or_log="print")
        >>> def simple_func(var1:str="this")->str:
        ...     return var1
        >>> simple_func()
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        # No error
        ```
        </div>

        ```{.py .python linenums="1" title="Example 2: Expected error"}
        >>> @retry(exceptions=TypeError, tries=5, delay=1, print_or_log="print")
        >>> def failing_func(var1:str="that")->None:
        ...     raise ValueError("Incorrect value")
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
    for param in ["tries", "delay"]:
        if not eval(param) >= 0:
            raise ValueError(
                f"Invalid value for parameter `{param}`: {eval(param)}\n"
                f"Must be a positive integer."
            )
    if print_or_log == "log":
        stk: inspect.FrameInfo = inspect.stack()[2]
        mod: Union[ModuleType, None] = inspect.getmodule(stk[0])
        if mod is not None:
            log: Optional[Logger] = logging.getLogger(mod.__name__)
    else:
        log = None

    def decorator(func: Callable):
        @wraps(func)
        def result(*args, **kwargs):
            for i in range(1, tries + 1):
                try:
                    results = func(*args, **kwargs)
                except exceptions as e:
                    # Catch raw exceptions as defined in the `exceptions` parameter.
                    message = (
                        f"Caught an expected error at iteration {i}: "
                        f"`{get_full_class_name(e)}`. "
                        f"Retrying in {delay} seconds..."
                    )
                    print_or_log_output(
                        message=message,
                        print_or_log=print_or_log,
                        log=log,
                        log_level="warning",
                    )
                    sleep(delay)
                except Exception as exc:
                    """
                    Catch unknown exception, however still need to check whether the name of any of the exceptions defined in `exceptions` are somehow listed in the text output of the caught exception.
                    The cause here is shown in the below chunk. You see here that it throws a 'Py4JJavaError', which was not listed in the `exceptions` parameter, yet within the text output, it showed the 'ConcurrentDeleteReadException' which _was_ listed in the `exceptions` parameter. Therefore, in this instance, we still want to sleep and retry

                    >>> Caught an unexpected error at iteration 1: `py4j.protocol.Py4JJavaError`.
                    >>> Time for fct_Receipt: 27secs
                    >>> java.util.concurrent.ExecutionException: io.delta.exceptions.
                    ...     ConcurrentDeleteReadException: This transaction attempted to read one or more files that were deleted (for example part-00001-563449ea-73e4-4d7d-8ba8-53fee1f8a5ff.c000.snappy.parquet in the root of the table) by a concurrent update. Please try the operation again.
                    """
                    excs = (
                        [exceptions]
                        if not isinstance(exceptions, (list, tuple))
                        else exceptions
                    )
                    exc_names = [exc.__name__ for exc in excs]
                    if any(name in f"{exc}" for name in exc_names):
                        caught_error = [name for name in exc_names if name in f"{exc}"]
                        message = (
                            f"Caught an unexpected, known error at iteration {i}: "
                            f"`{get_full_class_name(exc)}`.\n"
                            f"Who's message contains reference to underlying exception(s): {caught_error}.\n"
                            f"Retrying in {delay} seconds..."
                        )
                        print_or_log_output(
                            message=message,
                            print_or_log=print_or_log,
                            log=log,
                            log_level="warning",
                        )
                        sleep(delay)
                    else:
                        message = (
                            f"Caught an unexpected error at iteration {i}: "
                            f"`{get_full_class_name(exc)}`."
                        )
                        print_or_log_output(
                            message=message,
                            print_or_log=print_or_log,
                            log=log,
                            log_level="error",
                        )
                        raise RuntimeError(message) from exc
                else:
                    message = f"Successfully executed at iteration {i}."
                    print_or_log_output(
                        message=message,
                        print_or_log=print_or_log,
                        log=log,
                        log_level="info",
                    )
                    return results
            message = f"Still could not write after {tries} iterations. Please check."
            print_or_log_output(
                message=message,
                print_or_log=print_or_log,
                log=log,
                log_level="error",
            )
            raise RuntimeError(message)

        return result

    return decorator
