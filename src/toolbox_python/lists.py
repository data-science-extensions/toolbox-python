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
    The `lists` module is used to manipulate and enhance Python `#!py list`'s.
!!! abstract "Details"
    Note that functions in this module will only take-in and manipulate existing `#!py list` objects, and also output `#!py list` objects. It will not sub-class the base `#!py list` object, or create new '`#!py list`-like' objects. It will always maintain pure python types at it's core.
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
from typing import Any, Optional, Union

# ## Python Third Party Imports ----
from more_itertools import collapse as itertools_collapse
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.collection_types import any_list, any_tuple, collection, scalar


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
    list_of_lists: Union[scalar, collection],
    base_type: Optional[type] = None,
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
        list_of_lists (list[any_list]):
            The input `#!py list` of `#!py list`'s that you'd like to flatten to a single-level `#!py list`.
        base_type (Optional[type], optional):
            Binary and text strings are not considered iterable and will not be collapsed. To avoid collapsing other types, specify `base_type`.<br>
            Defaults to `#!py None`.
        levels (Optional[int], optional):
            Specify `levels` to stop flattening after a certain nested level.<br>
            Defaults to `#!py None`.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (any_list):
            The updated `#!py list`.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.lists import flatten
        ```

        ```{.py .python linenums="1" title="Example 1: Basic list, same input & output"}
        >>> print(flatten([0, 1, 2, 3]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 2: List containing two lists"}
        >>> print(flatten([[0, 1], [2, 3]]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 3: List containing a list and other data"}
        >>> print(flatten([0, 1, [2, 3]]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 4: List containing two lists and other data"}
        >>> print(flatten([[0, 1], [2, 3], 4, 5]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 5: List containing a list, a tuple, and other data"}
        >>> print(flatten([[0, 1], (2, 3), 4, 5]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 6: List containing up to three levels deep"}
        >>> print(flatten([[0, 1], [2, 3, [4, 5]]]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 7: List containing up to three levels deep, plus other data"}
        >>> print(flatten([[0, 1], [2, 3, [4, 5]], 6, 7]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5, 6, 7]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 8: List containing up to four levels deep"}
        >>> print(flatten([[0, 1], [2, 3, [4, [5]]]]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

    ??? tip "See Also"
        - [`more_itertools`](https://more-itertools.readthedocs.io/en/stable/api.html)
        - [`more_itertools.collapse()`](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.collapse)
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
        Take in any number of inputs, and output them all in to a single flat `#!py list`.

    Params:
        inputs (Any):
            Any input.

    Raises:
        TypeError: If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.

    Returns:
        (any_list):
            The input having been coerced to a single flat `#!py list`.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.lists import flat_list
        ```

        ```{.py .python linenums="1" title="Example 1: Basic input & output"}
        >>> print(flat_list(0, 1, 2, 3))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 2: Multiple lists"}
        >>> print(flat_list([0, 1], [2, 3]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 3: List and other data"}
        >>> print(flat_list(0, 1, [2, 3]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 4: Multiple lists and other data"}
        >>> print(flat_list([0, 1], [2, 3], 4, 5))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 5: List and a tuple and other data"}
        >>> print(flat_list([0, 1], (2, 3), 4, 5))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 6: List and a nested list"}
        >>> print(flat_list([0, 1], [2, 3, [4, 5]]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 7: List and a nested list and other data"}
        >>> print(flat_list([0, 1], [2, 3, [4, 5]], 6, 7))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5, 6, 7]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

        ```{.py .python linenums="1" title="Example 8: Deep nested lists"}
        >>> print(flat_list([0, 1], [2, 3, [4, [5]]]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [0, 1, 2, 3, 4, 5]
        ```
        !!! success "Conclusion: Successful flattening."
        </div>

    ??? tip "See Also"
        - [`flatten()`][toolbox_python.lists.flatten]
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

    Returns:
        (list[tuple[Any, ...]]):
            The updated `#!py list` list of `#!py tuple`'s representing the Cartesian product of the provided iterables.

    ???+ example "Examples"

        ```{.py .python linenums="1" title="Set up"}
        >>> from toolbox_python.lists import product
        ```

        ```{.py .python linenums="1" title="Example 1: Basic input & output"}
        >>> print(product([1], [11], [111]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [
            (1, 11, 111),
        ]
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 2: Multiple lists"}
        >>> print(product([1, 2], [11], [111]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [
            (1, 11, 111),
            (2, 11, 111),
        ]
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 3: List and other data"}
        >>> print(product([1, 2], [11], [111, 222]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [
            (1, 11, 111),
            (1, 11, 222),
            (2, 11, 111),
            (2, 11, 222),
        ]
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

        ```{.py .python linenums="1" title="Example 4: Multiple lists and other data"}
        >>> print(product([1, 2], [11, 22], [111, 222]))
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Terminal"}
        [
            (1, 11, 111),
            (1, 11, 222),
            (1, 22, 111),
            (1, 22, 222),
            (2, 11, 111),
            (2, 11, 222),
            (2, 22, 111),
            (2, 22, 222),
        ]
        ```
        !!! success "Conclusion: Successful conversion."
        </div>

    ??? tip "See Also"
        - [itertools](https://docs.python.org/3/library/itertools.html)
        - [itertools.product()](https://docs.python.org/3/library/itertools.html#itertools.product)
    """
    return list(itertools_product(*iterables))
