# ============================================================================ #
#                                                                              #
#     Title   : Classes                                                        #
#     Purpose : Contain functions which can be run on classes to extract       #
#               general information.                                           #
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
    The `classes` module is designed for functions to be executed _on_ classes; not _within_ classes.
    For any methods/functions that should be added _to_ classes, you should consider re-designing the original class, or sub-classing it to make further alterations.
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
from typing import Any

# ## Local First Party Imports ----
from toolbox_python.collection_types import str_list


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #


__all__: str_list = ["get_full_class_name", "class_property"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  get_full_class_name()                                                    ####
# ---------------------------------------------------------------------------- #


def get_full_class_name(obj: Any) -> str:
    """
    !!! note "Summary"
        This function is designed to extract the full name of a class, including the name of the module from which it was loaded.

    ???+ abstract "Details"
        Note, this is designed to retrieve the underlying _class name_ of an object, not the _instance name_ of an object. This is useful for debugging purposes, or for logging.

    Params:
        obj (Any):
            The object for which you want to retrieve the full name.

    Returns:
        (str):
            The full name of the class of the object.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.classes import get_full_class_name
        ```

        ```{.py .python linenums="1" title="Example 1: Check the name of a standard class"}
        >>> print(get_full_class_name(str))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        str
        ```
        !!! success "Conclusion: Successful class name extraction."
        </div>

        ```{.py .python linenums="1" title="Example 2: Check the name of an imported class"}
        >>> from random import Random
        >>> print(get_full_class_name(Random))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        random.Random
        ```
        !!! success "Conclusion: Successful class name extraction."
        </div>

    ??? success "Credit"
        Full credit goes to:<br>
        https://stackoverflow.com/questions/18176602/how-to-get-the-name-of-an-exception-that-was-caught-in-python#answer-58045927
    """
    module: str = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + "." + obj.__class__.__name__


class class_property:
    """
    !!! note "Summary"
        A decorator similar to `@property` but works on class methods instead of instance methods.

    ???+ abstract "Details"
        Allows defining class-level properties that are computed when accessed rather than stored.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.classes import class_property
        ```

        ```{.py .python linenums="1" title="Example 1: Create a class property"}
        >>> class MyClass:
        ...     _class_value: str = "original"
        ...
        ...     @class_property
        ...     def class_value(cls) -> str:
        ...         return cls._class_value
        ...
        >>> print(MyClass.class_value)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        original
        ```
        !!! success "Conclusion: Successful class property creation."
        </div>

        ```{.py .python linenums="1" title="Example 2: Create a class property with instance override"}
        >>> class MyClass:
        ...     _class_value: str = "original"
        ...
        ...     def __init__(self, instance_value: str = "instance") -> None:
        ...         self._instance_value = instance_value
        ...
        ...     @class_property
        ...     def class_value(cls) -> str:
        ...         return cls._class_value
        ...
        ...     @property
        ...     def instance_value(self) -> str:
        ...         return self._instance_value
        ...
        ...
        >>> my_instance = MyClass()
        >>> print(my_instance.class_value)
        >>> print(my_instance.instance_value)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        original
        instance
        ```
        !!! success "Conclusion: Successful class property with instance override."
        </div>
    """

    def __init__(self, method: Any) -> None:
        self.method: Any = method
        self.name: str = method.__name__
        self.__doc__ = method.__doc__

    def __get__(self, instance: Any, cls=None) -> Any:

        # Check for instance-level override
        if instance is not None:

            # Look for _attribute_name pattern
            private_name: str = f"_{self.name}"
            if hasattr(instance, private_name):
                return getattr(instance, private_name)

        # Fall back to class method
        return self.method(cls)
