from dataclasses import fields

import dash_table

from models.OtherSampleDataItem import OtherSampleDataItem
from service.data_provider import app_data_provider

"""
Component creation function for other sample data table
"""


def create_other_sample_data_table() -> dash_table.DataTable:
    # Get data
    data = [item.__dict__ for item in app_data_provider.get_other_sample_data()]
    # Create columns
    columns = [
        {
            "name": field.name.replace("_", " ").title(),
            "id": field.name
        }
        for field in fields(OtherSampleDataItem)
    ]
    # Create component
    return dash_table.DataTable(
        data=data,
        columns=columns,
        page_size=10
    )
