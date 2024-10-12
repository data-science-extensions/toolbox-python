# ============================================================================ #
#                                                                              #
#     Title   : Lists                                                          #
#     Purpose : Manipulate and enhance lists.                                  #
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
    The `lists` module is used how to manipulate and enhance Python lists.
!!! abstract "Details"
    Note that functions in this module will only take-in and manipulate existing `#!py list` objects, and also output `#!py list` objects. It will not sub-class the base `#!py list` object, or create new '`#!py list`-like' objects. It will always remain pure python types at it's core.
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
from itertools import product as itertools_product
from typing import Any, Optional

# ## Python Third Party Imports ----
from more_itertools import collapse as itertools_collapse
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import any_list, any_tuple


# ---------------------------------------------------------------------------- #
#  Exports                                                                  ####
# ---------------------------------------------------------------------------- #

__all__: list[str] = ["flatten", "flat_list", "product"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Functions                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def flatten(
    list_of_lists: any_list,
    base_type: Optional[Any] = None,
    levels: Optional[int] = None,
) -> any_list:
    """
    !!! note "Summary"
        For a given `#!py list` of `#!py list`'s, flatten it out to be a single `#!py list`.

    ???+ info "Details"
        Under the hood, this function will call the [`#!py more_itertools.collapse()`][more_itertools.collapse] function. The difference between this function and the [`#!py more_itertools.collapse()`][more_itertools.collapse] function is that the one from [`#!py more_itertools`][more_itertools] will return a `chain` object, not a `list` object. So, all we do here is call the [`#!py more_itertools.collapse()`][more_itertools.collapse] function, then parse the result in to a `#!py list()` function to ensure that the result is always a `#!py list` object.

        [more_itertools]: https://more-itertools.readthedocs.io/en/stable/api.html
        [more_itertools.collapse]: https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.collapse

    Params:
        list_of_lists (List[Any]):
            The input `#!py list` of `#!py list`'s that you'd like to flatten to a single-level `#!py list`.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (List[Any]):
            The updated `#!py list`.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)
    """
    return list(
        itertools_collapse(
            iterable=list_of_lists,
            base_type=base_type,
            levels=levels,
        )
    )


@typechecked
def flat_list(*inputs: Any) -> any_list:
    """
    !!! note "Summary"
        Take in any number of inputs, and output them all in to a single flat list.

    Params:
        inputs (Any):
            Any input.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (List[Any]):
            The input having been coerced to a single flat list.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)

    ??? tip "See Also"
        - [`flatten()`][python_helpers.lists.flatten]
    """
    return flatten(list(inputs))


def product(*iterables) -> list[any_tuple]:
    """
    !!! note "Summary"
        For a given number of `#!py iterables`, perform a cartesian product on them, and return the result as a list.

    ???+ info "Details"
        Under the hood, this function will call the [`#!py itertools.product()`][itertools.product] function. The difference between this function and the [`#!py itertools.product()`][itertools.product] function is that the one from [`#!py itertools`][itertools] will return a `product` object, not a `list` object. So, all we do here is call the [`#!py itertools.product()`][itertools.product] function, then parse the result in to a `#!py list()` function to ensure that the result is always a `#!py list` object.

        [itertools]: https://docs.python.org/3/library/itertools.html
        [itertools.product]: https://docs.python.org/3/library/itertools.html#itertools.product

    Params:
        iterables (Any):
            The input `#!py iterables` that you'd like to expand out.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (List[Tuple[Any]]):
            The updated `#!py list`.

    ???+ example "Examples"
        Please see: [Examples](../../usage/examples/)
    """
    return list(itertools_product(*iterables))
