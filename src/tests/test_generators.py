# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python Third Party Imports ----
from parameterized import parameterized
from pytest import raises

# ## Local First Party Imports ----
from tests.setup import name_func_predefined_name
from toolbox_python.generators import generate_group_cutoffs


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestCalculateGroupCutoffs:

    @parameterized.expand(
        input=(
            ("10x2", 10, 2, ((0, 5), (5, 11))),
            ("10x3", 10, 3, ((0, 3), (3, 6), (6, 11))),
            ("10x5", 10, 5, ((0, 2), (2, 4), (4, 6), (6, 8), (8, 11))),
            ("847834x2", 847834, 2, ((0, 423917), (423917, 847835))),
        ),
        name_func=name_func_predefined_name,
    )
    def test_calculate_group_cutoffs(
        self,
        name: str,
        number: int,
        groups: int,
        expected: tuple[tuple[int, int], ...],
    ) -> None:
        output: tuple[tuple[int, int], ...] = generate_group_cutoffs(number, groups)
        assert output == expected

    @parameterized.expand(
        input=(
            ("total", -5, 2),
            ("group", 10, -2),
            ("size", 5, 10),
        ),
        name_func=name_func_predefined_name,
    )
    def test_calculate_group_cutoffs_invalid(
        self,
        name: str,
        number: int,
        groups: int,
    ) -> None:
        with raises(ValueError):
            generate_group_cutoffs(number, groups)
