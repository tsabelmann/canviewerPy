"""Module stores the path to the top-level ui folder.
"""

# Import P
import pathlib

# PATHS
UI_PATH = pathlib.Path(__file__).parent.joinpath(pathlib.Path("../../ui/")).resolve()
