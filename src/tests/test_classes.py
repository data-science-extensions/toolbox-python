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
        self._instance_value = instance_value

    @class_property
    def class_value(cls) -> str:
        return cls._class_value

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

    def test_class_property_modified_properties(self) -> None:
        new_class = MyClass("instance value")
        assert new_class.instance_value == "instance value"
        new_class._instance_value = "new instance value"
        assert new_class.instance_value == "new instance value"
        new_class._class_value = "new class value"
        assert new_class.class_value == "new class value"

    def test_class_property_missing(self) -> None:
        with raises(AttributeError):
            MyClass().missing_property
        with raises(AttributeError):
            MyClass.missing_property
        with raises(AttributeError):
            MyClass().missing_class_property
        with raises(AttributeError):
            MyClass.missing_class_property
