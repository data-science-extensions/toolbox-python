# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from itertools import product as itertools_product
from unittest import TestCase

# ## Local First Party Imports ----
from toolbox_python.lists import flat_list, flatten, product


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  flatten()                                                                ####
# ---------------------------------------------------------------------------- #


class TestFlatten(TestCase):

    def setUp(self) -> None:
        pass

    def test_flatten_1(self) -> None:
        _input = [0, 1, 2, 3]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3]
        assert _output == _expected

    def test_flatten_2(self) -> None:
        _input = [[0, 1], [2, 3]]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3]
        assert _output == _expected

    def test_flatten_3(self) -> None:
        _input = [0, 1, [2, 3]]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3]
        assert _output == _expected

    def test_flatten_4(self) -> None:
        _input = [[0, 1], [2, 3], 4, 5]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected

    def test_flatten_5(self) -> None:
        _input = [[0, 1], (2, 3), 4, 5]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected

    def test_flatten_6(self) -> None:
        _input = [[0, 1], [2, 3, [4, 5]]]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected

    def test_flatten_7(self) -> None:
        _input = [[0, 1], [2, 3, [4, 5]], 6, 7]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3, 4, 5, 6, 7]
        assert _output == _expected

    def test_flatten_8(self) -> None:
        _input = [[0, 1], [2, 3, [4, [5]]]]
        _output = flatten(_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected


# ---------------------------------------------------------------------------- #
#  flat_list()                                                              ####
# ---------------------------------------------------------------------------- #


class TestFlatList(TestCase):

    def setUp(self) -> None:
        pass

    def test_flat_list_1(self) -> None:
        _input = [0, 1, 2, 3]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3]
        assert _output == _expected

    def test_flat_list_2(self) -> None:
        _input = [[0, 1], [2, 3]]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3]
        assert _output == _expected

    def test_flat_list_3(self) -> None:
        _input = [0, 1, [2, 3]]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3]
        assert _output == _expected

    def test_flat_list_4(self) -> None:
        _input = [[0, 1], [2, 3], 4, 5]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected

    def test_flat_list_5(self) -> None:
        _input = [[0, 1], (2, 3), 4, 5]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected

    def test_flat_list_6(self) -> None:
        _input = [[0, 1], [2, 3, [4, 5]]]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected

    def test_flat_list_7(self) -> None:
        _input = [[0, 1], [2, 3, [4, 5]], 6, 7]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3, 4, 5, 6, 7]
        assert _output == _expected

    def test_flat_list_8(self) -> None:
        _input = [[0, 1], [2, 3, [4, [5]]]]
        _output = flat_list(*_input)
        _expected = [0, 1, 2, 3, 4, 5]
        assert _output == _expected


# ---------------------------------------------------------------------------- #
#  product()                                                                ####
# ---------------------------------------------------------------------------- #


class TestProduct(TestCase):

    def setUp(self) -> None:
        pass

    def test_product_1(self) -> None:
        _input = [[1], [11], [111]]
        _output = product(*_input)
        _expected = list(itertools_product(*_input))
        assert _output == _expected

    def test_product_2(self) -> None:
        _input = [[1, 2], [11], [111]]
        _output = product(*_input)
        _expected = list(itertools_product(*_input))
        assert _output == _expected

    def test_product_3(self) -> None:
        _input = [[1, 2], [11], [111, 222]]
        _output = product(*_input)
        _expected = list(itertools_product(*_input))
        assert _output == _expected

    def test_product_4(self) -> None:
        _input = [[1, 2], [11, 22], [111, 222]]
        _output = product(*_input)
        _expected = list(itertools_product(*_input))
        assert _output == _expected
