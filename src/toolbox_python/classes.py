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
from functools import wraps
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


# TODO: This can still be made to work for setters by implementing an accompanying metaclass that supports it.
class class_property(property):
    """
    !!! note "Summary"
        Similar to `property`, but allows class-level properties. That is, a property whose getter is like a `classmethod`.

    ???+ abstract "Details"
        The wrapped method may explicitly use the `classmethod` decorator (which must become before this decorator), or the `classmethod` may be omitted (it is implicit through use of this decorator).

    Params:
        fget (callable):
            The function that computes the value of this property (in particular, the function when this is used as a decorator) a la `property`.

        doc (str, optional):
            The docstring for the property--by default inherited from the getter function.

    ???+ example "Examples"

        Normal usage is as a decorator:

        ```{.py .python linenums="1" title="Example 1: Normal usage"}
        >>> class Foo:
        ...     _bar_internal = 1
        ...
        ...     @class_property
        ...     def bar(cls):
        ...         return cls._bar_internal + 1
        >>>
        >>> print(f"Class attribute: `{Foo.bar}`")
        >>>
        >>> foo_instance = Foo()
        >>> print(f"Instantiated class: `{foo_instance.bar}`")
        >>>
        >>> foo_instance._bar_internal = 2
        >>> print(f"Modified instance attribute: `{foo_instance.bar}`")  # Ignores instance attributes
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        Class attribute: `2`
        Instantiated class: `2`
        Modified instance attribute: `2`
        ```
        Note that in the third `print()` statement, the instance attribute `_bar_internal` is ignored. This is because `class_property` is designed to be used as a class-level property, not an instance-level property. See the Notes section for more details.
        !!! success "Conclusion: Successful usage."
        </div>

        As previously noted, a `class_property` is limited to implementing read-only attributes:

        ```{.py .python linenums="1" title="Example 2: Read-only attributes"}
        >>> class Foo:
        ...     _bar_internal = 1
        ...
        ...     @class_property
        ...     def bar(cls):
        ...         return cls._bar_internal
        ...
        ...     @bar.setter
        ...     def bar(cls, value):
        ...         cls._bar_internal = value
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        Traceback (most recent call last):
        ...
        NotImplementedError: class_property can only be read-only; use a metaclass to implement modifiable class-level properties
        ```
        !!! failure "Conclusion: Failed to set a class property."
        </div>

    ???+ info "Notes"
        - `@class_property` only works for *read-only* properties. It does not currently allow writeable/deletable properties, due to subtleties of how Python descriptors work. In order to implement such properties on a class, a metaclass for that class must be implemented.
        - `@class_property` is not a drop-in replacement for `property`. It is designed to be used as a class-level property, not an instance-level property. If you need to use it as an instance-level property, you will need to use the `@property` decorator instead.
        - `@class_property` is defined at class scope, not instance scope. This means that it is not bound to the instance of the class, but rather to the class itself; hence the name `class_property`. This means that it is designed to be used as a class-level property and is accessed through the class itself, not an instance-level property which is accessed through the instance of a class. If it is necessary to access the instance-level property, you will need to use the instance itself (eg. `instantiated_class_name._internal_attribute`) or create an instance-level property using the `@property` decorator.

    ???+ success "Credit"
        This `@class_property` object is heavily inspired by the [`astropy`](https://www.astropy.org/) library. All credit goes to them. See: [details](https://github.com/astropy/astropy/blob/e4993fffb54e19b04bc4e9af084984650bc0a46f/astropy/utils/decorators.py#L551-L722).
    """

    def __new__(cls, fget=None, doc=None):

        if fget is None:

            # Being used as a decorator-return a wrapper that implements decorator syntax
            def wrapper(func):
                return cls(func, doc=doc)

            return wrapper

        return super().__new__(cls)

    def __init__(self, fget, doc=None):

        fget = self._wrap_fget(fget)
        super().__init__(fget=fget, doc=doc)

        # There is a bug in Python where `self.__doc__` doesn't get set properly on instances of property subclasses if the `doc` argument was used rather than taking the docstring from `fget`.
        # Related Python issue: https://bugs.python.org/issue24766
        if doc is not None:
            self.__doc__ = doc

    def __get__(self, obj, objtype) -> Any:  # type: ignore[override]
        # The base `property.__get__` will just return self here; instead we pass `objtype` through to the original wrapped function (which takes the `class` as its sole argument). This is how we obtain the `class` attribute and not the `instance` attribute, and the key difference between `@property` and `@class_property`. This is also the same as `classmethod.__get__()`, but we need to pass `objtype` rather than `obj` to the wrapped function.
        val: Any = self.fget.__wrapped__(objtype)  # type: ignore[union-attr]
        return val

    @staticmethod
    def _wrap_fget(orig_fget):
        if isinstance(orig_fget, classmethod):
            orig_fget = orig_fget.__func__

        # Using standard `functools.wraps` for simplicity.
        @wraps(orig_fget)  # pragma: no cover
        def fget(obj):
            return orig_fget(obj.__class__)

        return fget

    # def getter(self, fget) -> property:
    #     return super().getter(self._wrap_fget(fget))

    def setter(self, fset) -> Any:
        raise NotImplementedError(
            "class_property can only be read-only; use a metaclass to implement modifiable class-level properties"
        )

    def deleter(self, fdel) -> Any:
        raise NotImplementedError(
            "class_property can only be read-only; use a metaclass to implement modifiable class-level properties"
        )


# def cached_class_property(func) -> property:
#     """
#     !!! note "Summary"
#         This function is designed to cache the result of a class property, so that it is only computed once, and then stored for future reference.

#     ???+ abstract "Details"
#         This is useful for properties that are computationally expensive, but are not expected to change over the lifetime of the object.

#     Params:
#         func (Callable):
#             The function to be cached.

#     Returns:
#         (property):
#             The cached property.

#     ???+ example "Examples"

#         ```{.py .python linenums="1" title="Set up"}
#         >>> from toolbox_python.classes import cached_class_property
#         ```

#         ```{.py .python linenums="1" title="Example 1: Create a cached class property"}
#         >>> class TestClass:
#         ...     @cached_class_property
#         ...     def expensive_property(cls):
#         ...         print("Computing expensive property...")
#         ...         return 42
#         ...
#         >>> print(TestClass.expensive_property)
#         >>> print(TestClass.expensive_property)
#         ```
#         <div class="result" markdown>
#         ```{.sh .shell title="Terminal"}
#         Computing expensive property...
#         42
#         42
#         ```
#         !!! success "Conclusion: Successful property caching."
#         </div>
#     """
#     attr_name = "_cached_" + func.__name__

#     @property
#     @wraps(func)
#     def wrapper(self):
#         if not hasattr(self, attr_name):
#             setattr(self, attr_name, func(self))
#         return getattr(self, attr_name)

#     return wrapper
