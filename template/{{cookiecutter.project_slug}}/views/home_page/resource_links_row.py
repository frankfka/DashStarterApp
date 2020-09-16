import dash_core_components as dcc
import dash_bootstrap_components as dbc

from views.home_page.styles import *

LINKS = [
    ('Dash Docs', 'https://dash.plotly.com/'),
    ('App Gallery', 'https://dash-gallery.plotly.host/Portal/'),
    ('Starter App Repo', ''),  # TODO
    ('Bootstrap Components', 'https://dash-bootstrap-components.opensource.faculty.ai/')
]


def __create_link__(name: str, href: str) -> dbc.Col:
    return dcc.Link(name, href=href, style=RESOURCE_LINK_STYLE, target='_blank')


def create_resource_links_row() -> dbc.Row:
    return dbc.Row(
        children=[
            __create_link__(link[0], link[1]) for link in LINKS
        ],
        justify='center',
        style=RESOURCE_LINKS_ROW_STYLE
    )
