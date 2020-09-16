import pathlib

from app import main_app


"""
This file holds common utility functions to be used throughout the Dash app.
"""

__root_path__ = pathlib.Path(__file__).parent


def get_path(relative_path: str) -> pathlib.Path:
    """
    Utility to retrieve correct path to any project file given a relative path to the root of the project directory
    """
    return __root_path__.joinpath(relative_path)


def get_asset_path(relative_path_in_assets: str):
    """
    Uses the Dash app utility to retrieve an asset from /assets. For example, a file /assets/some_folder/file.txt
    can be retrieved using get_asset_path("some_folder/file.txt"). Using this is required when deploying with Dash
    Enterprise.
    """
    return main_app.get_asset_url(relative_path_in_assets)
