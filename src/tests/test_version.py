# ---------------------------------------------------------------------------- #
#                                                                              #
#     Setup                                                                 ####
#                                                                              #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#  Imports                                                                  ####
# ---------------------------------------------------------------------------- #


# ## Python StdLib Imports ----
from unittest import TestCase

# ## Local First Party Imports ----
from toolbox_python import __version__ as version


# ---------------------------------------------------------------------------- #
#  Constants                                                                ####
# ---------------------------------------------------------------------------- #


__version__ = "v1.4.0"


# ---------------------------------------------------------------------------- #
#                                                                              #
#     Test Suite                                                            ####
#                                                                              #
# ---------------------------------------------------------------------------- #


class TestStrings(TestCase):
    def setUp(self) -> None:
        pass

    def test_version(self) -> None:
        assert version == __version__
