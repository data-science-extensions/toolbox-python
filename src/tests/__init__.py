"""
Due to the way that this directory structure is set up, we need to ensure that the `path` is correctly able to access the modules within the `src` directory.
"""

# ## Python StdLib Imports ----
import os
import sys


### Ensure `path` is configured correctly ----
if os.path.abspath("./src") not in sys.path:
    sys.path.append(os.path.abspath("./src"))
