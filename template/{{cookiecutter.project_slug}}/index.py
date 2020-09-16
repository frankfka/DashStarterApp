import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import main_app
from config import app_config
from views import pages
from views.common_components.nav_bar import create_navbar
import views.routes as routes

"""
This file is the entrypoint for the Dash app. It contains the base layout for the Dash application, and handles
URL routing through the `dcc.Location` component.
"""

# Declare the root layout for the Dash app
main_app.layout = html.Div([
    # Hidden component that gives access to the URL path the user is requesting
    dcc.Location(id='url', refresh=False),
    # Navigation Bar
    html.Div(id='navbar'),
    # Main page content
    html.Div(id='page-content')
])


@main_app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """
    Displays the correct page corresponding to the URL that the user is on

    :param pathname: The relative URL path, such as /graph, that is provided by the dcc.Location component
    :return: The appropriate page for the relative URL
    """
    # Retrieve the appropriate layout
    layout = pages.get(pathname, None)
    if layout:
        return layout
    else:
        # No layout specified, just return 404 - alternatively, return a prettified Page Not Found layout
        return '404'


@main_app.callback(
    Output('navbar', 'children'),
    [Input('url', 'pathname')]
)
def update_navbar(pathname):
    """
    Updates the navigation bar corresponding to the URL that the user is on

    :param pathname: The relative URL path, such as /graph, that is provided by the dcc.Location component
    :return: The rendered navigation bar for the relative URL
    """
    return create_navbar(
        brand_name=app_config.app_name,
        brand_path=routes.HOME_ROUTE,
        nav_links=[
            ("Home", routes.HOME_ROUTE, pathname == routes.HOME_ROUTE),
            ("Graphs", routes.GRAPHS_PAGE_ROUTE, pathname == routes.GRAPHS_PAGE_ROUTE)
        ]
    )


# Expose the server instance
server = main_app.server

if __name__ == '__main__':
    main_app.run_server(debug=True)
