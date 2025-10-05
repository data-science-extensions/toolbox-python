# ============================================================================ #
#                                                                              #
#     Title   : Generators                                                     #
#     Purpose : Generate information as needed.                                #
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
    This module provides functions to generate information as needed. Such functions are typically used to generate data that is not stored in a database or file, but rather computed on-the-fly based on input parameters.
"""


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Import                                                                  ####
## --------------------------------------------------------------------------- #


# ## Python Third Party Imports ----
from typeguard import typechecked

# ## Local First Party Imports ----
from toolbox_python.checkers import assert_is_valid
from toolbox_python.collection_types import str_list


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: str_list = ["generate_group_cutoffs"]


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Groupings                                                             ####
#                                                                              #
# ---------------------------------------------------------------------------- #


@typechecked
def generate_group_cutoffs(
    total_number: int,
    num_groups: int,
) -> tuple[tuple[int, int], ...]:
    """
    !!! note "Summary"
        Generate group cutoffs for a given total number and number of groups.

    !!! abstract "Details"
        This function divides a total number of items into a specified number of groups, returning a `#!py tuple` of `#!py tuple`'s where each inner `#!py tuple` contains the start and end indices for each group. The last group may contain fewer items if the total number is not evenly divisible by the number of groups.

    Params:
        total_number (int):
            The total number of items to be divided into groups.
        num_groups (int):
            The number of groups to create.

    Raises:
        (TypeCheckError):
            If any of the inputs parsed to the parameters of this function are not the correct type. Uses the [`@typeguard.typechecked`](https://typeguard.readthedocs.io/en/stable/api.html#typeguard.typechecked) decorator.
        (ValueError):
            If `total_number` is less than 1, or if `num_groups` is less than 1, or if `total_number` is less than `num_groups`. Uses the [`assert_is_valid`][toolbox_python.checkers.assert_is_valid] function to validate the inputs.

    Returns:
        (tuple[tuple[int, int], ...]):
            A tuple of tuples, where each inner tuple contains the start and end indices for each group. The last group may have a different size if the total number is not evenly divisible by the number of groups.

    ???+ example "Examples"

        ```pycon {.py .python linenums="1" title="Prepare data"}
        >>> from toolbox_python.generators import generate_group_cutoffs
        ```

        ```pycon {.py .python linenums="1" title="Example 1: Basic usage"}
        >>> generate_group_cutoffs(10, 3)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ((0, 3), (3, 6), (6, 11))
        ```
        !!! success "Conclusion: Successfully split 10 items into 3 groups."
        </div>

        ```pycon {.py .python linenums="1" title="Example 2: Uneven groups"}
        >>> generate_group_cutoffs(10, 4)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ((0, 3), (3, 6), (6, 9), (9, 11))
        ```
        !!! success "Conclusion: Successfully split 10 items into 4 groups, with the last group having fewer items."
        </div>

        ```pycon {.py .python linenums="1" title="Example 3: Single group"}
        >>> generate_group_cutoffs(10, 1)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ((0, 11),)
        ```
        !!! success "Conclusion: Successfully created a single group containing all items."
        </div>

        ```pycon {.py .python linenums="1" title="Example 4: Zero groups"}
        >>> generate_group_cutoffs(10, 0)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ValueError: Validation failed: 'num_groups > 0' is not True
        ```
        !!! failure "Conclusion: Cannot create groups with zero groups specified."
        </div>

        ```pycon {.py .python linenums="1" title="Example 5: Negative total number"}
        >>> generate_group_cutoffs(-10, 3)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ValueError: Validation failed: 'total_number > 0' is not True
        ```
        !!! failure "Conclusion: Total number must be greater than 0."
        </div>

        ```pycon {.py .python linenums="1" title="Example 6: Total number less than groups"}
        >>> generate_group_cutoffs(3, 5)
        ```
        <div class="result" markdown>
        ```{.sh .shell title="Output"}
        ValueError: Validation failed: 'total_number >= num_groups' is not True
        ```
        !!! failure "Conclusion: Total number must be greater than or equal to the number of groups."
        </div>
    """

    # Validations
    assert_is_valid(total_number, ">", 0)
    assert_is_valid(num_groups, ">", 0)
    assert_is_valid(total_number, ">=", num_groups)

    # Calculate the size of each group
    group_size: int = total_number // num_groups

    # List to store all group cutoffs
    cutoffs: list[tuple[int, int]] = []

    # Calculate the number of items that will be in the last group
    current_start: int = 0

    # Loop through the number of groups to calculate start and end indices
    for group in range(num_groups):

        # For the last group, end is total_number + 1
        if group == num_groups - 1:
            current_end: int = total_number + 1
        else:
            current_end: int = current_start + group_size

        # Add the current group cutoff to the list
        cutoffs.append((current_start, current_end))

        # Update the start index for the next group
        current_start: int = current_end

    # Convert the list to a tuple of tuples
    return tuple(cutoffs)
