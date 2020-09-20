import pathlib

"""
This file holds common utility functions to be used throughout the Dash app.
"""

__root_path__ = pathlib.Path(__file__).parent


def get_path(relative_path: str) -> pathlib.Path:
    """
    Utility to retrieve correct path to any project file given a relative path to the root of the project directory
    """
    return __root_path__.joinpath(relative_path)
