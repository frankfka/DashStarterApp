import dash
from dash_bootstrap_components.themes import FLATLY

from config import app_config

"""
This file creates the main Dash app instance
"""

# Global stylesheets
stylesheets = [
    FLATLY
]

# Create the Dash app
main_app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=stylesheets,
    title=app_config.app_name,
    update_title=app_config.update_title
)


