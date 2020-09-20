import dash_bootstrap_components as dbc
import dash_html_components as html

from app import main_app
from views.home_page.resource_links_row import create_resource_links_row
from views.routes import GRAPHS_PAGE_ROUTE
from views.home_page.styles import *

"""
Main layout for the home page
"""

layout = html.Div(
    [
        # Logo
        html.Img(src=main_app.get_asset_url('img/logo.jpg'), style=HEADER_IMG_STYLE),
        # Header
        html.H1('Welcome to Your Dash App', style=WELCOME_TXT_STYLE),
        # Resources
        create_resource_links_row(),
        # Button to navigate to graphs page
        dbc.Button(
            'Graphs Page',
            href=GRAPHS_PAGE_ROUTE,
            size="lg"
        ),
    ],
    className="app-page"
)
