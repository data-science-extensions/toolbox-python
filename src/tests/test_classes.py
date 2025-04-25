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

# ## Python Third Party Imports ----
from pytest import raises

# ## Local First Party Imports ----
from toolbox_python.classes import (  # cached_class_property,
    class_property,
    get_full_class_name,
)
from toolbox_python.defaults import Defaults


# ---------------------------------------------------------------------------- #
#                                                                              #
#     get_full_class_name()                                                 ####
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


# ---------------------------------------------------------------------------- #
#                                                                              #
#     class_property()                                                      ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class MyClass:
    _class_value: str = "original"

    def __init__(self, instance_value: str = "instance") -> None:
        self._instance_value: str = instance_value

    @class_property
    def class_value(cls) -> str:
        return cls._class_value

    # @class_value.getter
    # def class_value_getter(cls) -> str:
    #     return cls._class_value

    @class_property
    def class_value_modified(cls) -> str:
        return cls._class_value + " modified"

    @class_property()
    def class_value_with_parens(cls) -> str:
        return cls._class_value + " with parens"

    @class_property(doc="This is a class property with a docstring.")
    def class_value_with_doc(cls) -> str:
        """This is a class property with a docstring."""
        return cls._class_value + " with doc"

    @class_property
    @classmethod
    def class_value_method(cls) -> str:
        """This is a class method."""
        return cls._class_value + " with method"

    @property
    def instance_value(self) -> str:
        return self._instance_value


class TestClassProperty(TestCase):

    def setUp(self) -> None:
        MyClass._class_value = "original"

    def test_class_property_class_property(self) -> None:
        assert MyClass.class_value == "original"

    def test_class_property_class_property_modified(self) -> None:
        MyClass._class_value = "modified"
        assert MyClass.class_value == "modified"

    def test_class_property_instance_property(self) -> None:
        assert MyClass().instance_value == "instance"

    def test_class_property_properties(self) -> None:
        new_class = MyClass()
        assert new_class.class_value == "original"
        assert new_class.instance_value == "instance"

    # def test_class_property_getter(self) -> None:
    #     assert MyClass.class_value_getter == MyClass.class_value

    def test_class_property_modified_properties(self) -> None:

        # Test the instance property for an instance of MyClass
        new_class = MyClass("instance value")
        assert new_class.instance_value == "instance value"

        # Test the modified value of an instance property for the instantiated class
        new_class._instance_value = "new instance value"
        assert new_class.instance_value == "new instance value"

        # Test the class property for an instance of MyClass
        # This should return the original class value, not the modified one
        new_class._class_value = "new class value"
        assert new_class.class_value == "original"

    def test_class_property_with_parens(self) -> None:
        assert MyClass.class_value_with_parens == "original with parens"
        MyClass._class_value = "modified"
        assert MyClass.class_value_with_parens == "modified with parens"

    def test_class_property_with_doc(self) -> None:
        assert MyClass.class_value_with_doc == "original with doc"
        MyClass.class_value_with_doc.__doc__ == (
            "This is a class property with a docstring."
        )

    def test_class_property_errors(self) -> None:
        with raises(AttributeError):
            MyClass().missing_property
        with raises(AttributeError):
            MyClass.missing_property
        with raises(AttributeError):
            MyClass().missing_class_property
        with raises(AttributeError):
            MyClass.missing_class_property

    def test_class_property_setter(self) -> None:

        with raises(NotImplementedError):

            class MyClassWithSetter:
                _class_value: str = "original"

                @class_property
                def class_value(cls) -> str:
                    return cls._class_value

                @class_value.setter
                def class_value(cls, value: str) -> None:
                    cls._class_value = value

    def test_class_property_deleter(self) -> None:

        with raises(NotImplementedError):

            class MyClassWithDeleter:
                _class_value: str = "original"

                @class_property
                def class_value(cls) -> str:
                    return cls._class_value

                @class_value.deleter
                def class_value(cls) -> None:
                    del cls._class_value
