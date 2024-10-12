# ============================================================================ #
#                                                                              #
#     Title   : Defaults                                                       #
#     Purpose : Enable setting and utilisation of default values.              #
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
    The `defaults` module is used how to set and control default values for our various Python processes.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Future Python Library Imports ----
from __future__ import annotations

# ## Python StdLib Imports ----
from typing import Any, Optional, Union

# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.bools import strtobool
from toolbox_python.checkers import is_type


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #


__all__: list[str] = ["defaults", "Defaults"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Classes                                                               ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Defaults Class                                                           ####
# ---------------------------------------------------------------------------- #


class Defaults:
    """
    !!! note "Summary"
        When we create and use Python variables, it is sometimes handy to add a default value for that variable.
        This class will handle that process.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    !!! success "Credit"
        Inspiration from:<br>
        https://github.com/henriquebastos/python-decouple/
    """

    def __init__(self) -> None:
        """
        !!! note "Summary"
            Nothing is initialised when this class is instantiated.
            Use the [`__call__()`][toolbox_python.defaults.Defaults.__call__] method instead.

        !!! tip "See Also"
            - [`Defaults.__call__()`][toolbox_python.defaults.Defaults.__call__]
        """
        return None

    def __call__(self, *args, **kwargs) -> Any:
        """
        !!! note "Summary"
            When this class is called, it will pass through all parameters to the internal [`.get()`][toolbox_python.defaults.Defaults.get] method.

        !!! tip "See Also"
            - [`Defaults.get()`][toolbox_python.defaults.Defaults.get]
        """
        return self.get(*args, **kwargs)

    @typechecked
    def get(
        self,
        value: Any,
        default: Optional[Any] = None,
        cast: Optional[Union[str, type]] = None,
    ) -> Any:
        """
        !!! note "Summary"
            From the value that is parsed in to the `value` parameter, convert it to `default` if `value` is `#!py None`, and convert it to `cast` if `cast` is not `#!py None`.

        ???+ info "Details"
            The detailed steps will be:

            1. Validate the input (using the internal [`._validate_value_and_default()`][toolbox_python.defaults.Defaults._validate_value_and_default] & [`._validate_type()`][toolbox_python.defaults.Defaults._validate_type] methods),
            1. If `value` is `#!py None`, then assign `default` to `value`.
            1. If `cast` is _not_ `#!py None`, then cast `value` to the data type in `cast`.
                - Note, `cast` can be _either_ the actual type to convert to, _or_ a string representation of the type.
            1. Return the updated/defaulted/casted `value` back to the user.

        Params:
            value (Any):
                The value to check.
            default (Optional[Any], optional):
                The default value for `value`.<br>
                Note, can be a `#!py None` value; however, if `value` is also `#!py None`, then `default` _cannot_ be `#!py None`.<br>
                Defaults to `#!py None`.
            cast (Optional[Union[str, type]], optional):
                The data type to convert to.<br>
                Must be one of: `#!py ["bool", "dict", "int", "float", "list", "str", "tuple"]`.<br>
                Defaults to `#!py None`.

        Returns:
            value (Any):
                The updated/defaulted/casted value.

        !!! tip "See Also"
            - [`Defaults._validate_value_and_default()`][toolbox_python.defaults.Defaults._validate_value_and_default]
            - [`Defaults._validate_type()`][toolbox_python.defaults.Defaults._validate_type]
        """
        (
            self._validate_value_and_default(
                value=value, default=default
            )._validate_type(check_type=cast)
        )
        if value is None:
            value = default
        if cast is not None:
            if (cast is bool or cast == "bool") and is_type(value, str):
                value = bool(strtobool(value))
            elif isinstance(cast, str):
                value = eval(cast)(value)
            else:
                value = cast(value)
        return value

    def _validate_value_and_default(
        self,
        value: Optional[Any] = None,
        default: Optional[Any] = None,
    ) -> Defaults:
        """
        !!! note "Summary"
            Validate to ensure that `value` and `default` are not both `#!py None`.

        Params:
            value (Optional[Any], optional):
                The `value` to check.<br>
                Defaults to `#!py None`.
            default (Optional[Any], optional):
                The `default` value to check.<br>
                Defaults to `#!py None`.

        Raises:
            AttributeError: If both `value` and `default` are `#!py None`.

        Returns:
            self (Defaults):
                If both `value` and `default` are not both `#!py None`, then return `self`.

        !!! tip "See Also"
            - [`Defaults.get()`][toolbox_python.defaults.Defaults.get]
        """
        if value is None and default is None:
            raise AttributeError(
                f"Both `value` and `default` are blank: '{value}', '{default}'.\n"
                f"If `value` is blank, then `default` cannot be blank."
            )
        return self

    def _validate_type(
        self,
        check_type: Optional[Union[str, type]] = None,
    ) -> Defaults:
        """
        !!! note "Summary"
            Check to ensure that `check_type` is a valid Python type.<br>
            Must be one of: `#!py ["bool", "dict", "int", "float", "list", "str", "tuple"]`.

        Params:
            check_type (Optional[Union[str, type]], optional):
                The type to check against. Can either be an actual Python type, or it's string representation.<br>
                Defaults to `#!py None`.

        Raises:
            AttributeError: If `check_type` is _both_ not `#!py None` _and_ if it is not one of the valid Python types.

        Returns:
            self (Defaults):
                If the type is valid, return `self`.

        !!! tip "See Also"
            - [`Defaults.get()`][toolbox_python.defaults.Defaults.get]
        """
        valid_types: list[str] = [
            "bool",
            "dict",
            "int",
            "float",
            "list",
            "str",
            "tuple",
        ]
        if check_type is None:
            return self
        elif is_type(check_type, str):
            retype = check_type
        elif type(check_type).__name__ == "type":
            retype = check_type.__name__  # type: ignore
        if retype is not None and retype not in valid_types:
            raise AttributeError(
                f"The value for `type` is invalid: `{retype}`.\n"
                f"Must be a valid type: {valid_types}."
            )
        return self


# ---------------------------------------------------------------------------- #
#  Instantiations                                                           ####
# ---------------------------------------------------------------------------- #


defaults = Defaults()
