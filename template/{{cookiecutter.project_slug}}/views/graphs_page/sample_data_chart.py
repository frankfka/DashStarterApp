import dash_core_components as dcc
import plotly.express as px

from service.data_provider import app_data_provider


"""
Component creation function for sample data chart
"""


def create_sample_data_chart() -> dcc.Graph:
    # Get data
    df = app_data_provider.get_sample_data_df()
    # Create figure
    fig = px.line(
        df, x="date", y="value",
        labels={
            "date": "Year",
            "value": "Value",
        },
    )
    # Update styles
    fig.update_layout(
        plot_bgcolor="ghostwhite",
        paper_bgcolor="ghostwhite"
    )
    # Create component
    return dcc.Graph(
        id="sample-data-chart",
        figure=fig,
    )
