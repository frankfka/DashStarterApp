import dash_core_components as dcc
import dash_html_components as html

from views.graphs_page.other_sample_data_table import create_other_sample_data_table
from views.graphs_page.sample_data_chart import create_sample_data_chart
from views.graphs_page.styles import *

"""
Main layout for the graphs page.
"""

layout = html.Div(
    [
        html.H1('Graphs', style=TITLE_STYLE),
        # Sample Data Chart
        html.Div(
            [
                html.H3("Sample Data Chart"),
                create_sample_data_chart(),
            ],
            style=CHART_ITEM_STYLE
        ),
        # Other Sample Data Table
        html.Div(
            [
                html.H3("Other Sample Data Table"),
                create_other_sample_data_table(),
            ],
            style=CHART_ITEM_STYLE
        )
    ],
    className="app-page",
    style=PAGE_STYLE
)
