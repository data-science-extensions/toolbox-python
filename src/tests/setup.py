# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from typing import Callable

# ## Local First Party Imports ----
from toolbox_python.collection_types import any_collection


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: list[str] = [
    "name_func_flat_list",
    "name_func_nested_list",
]

## --------------------------------------------------------------------------- #
##  Helper functions                                                        ####
## --------------------------------------------------------------------------- #


def name_func_flat_list(
    func: Callable,
    idx: int,
    params: any_collection,
) -> str:
    return f"{func.__name__}_{int(idx)+1:02}_{'_'.join([str(param) for param in params[0]])}"


def name_func_nested_list(
    func: Callable,
    idx: int,
    params: list[any_collection] | tuple[any_collection],
) -> str:
    return f"{func.__name__}_{int(idx)+1:02}_{params[0][0]}_{params[0][1]}"


def name_func_predefined_name(
    func: Callable,
    idx: int,
    params: any_collection,
) -> str:
    return f"{func.__name__}_{int(idx)+1:02}_{params[0][0]}"
