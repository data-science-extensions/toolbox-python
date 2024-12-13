# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


## --------------------------------------------------------------------------- #
##  Imports                                                                 ####
## --------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from typing import Callable, Union

# ## Local First Party Imports ----
from toolbox_python.collection_types import any_list_tuple, str_list


## --------------------------------------------------------------------------- #
##  Exports                                                                 ####
## --------------------------------------------------------------------------- #


__all__: str_list = [
    "name_func_flat_list",
    "name_func_nested_list",
    "name_func_predefined_name",
]


## --------------------------------------------------------------------------- #
##  Helper functions                                                        ####
## --------------------------------------------------------------------------- #


def name_func_flat_list(
    func: Callable,
    idx: int,
    params: any_list_tuple,
) -> str:
    return f"{func.__name__}_{int(idx)+1:02}_{'_'.join([str(param) for param in params[0]])}"


def name_func_nested_list(
    func: Callable,
    idx: int,
    params: Union[list[any_list_tuple,], tuple[any_list_tuple,]],
) -> str:
    return f"{func.__name__}_{int(idx)+1:02}_{params[0][0]}_{params[0][1]}"


def name_func_predefined_name(
    func: Callable,
    idx: int,
    params: any_list_tuple,
) -> str:
    return f"{func.__name__}_{int(idx)+1:02}_{params[0][0]}"
