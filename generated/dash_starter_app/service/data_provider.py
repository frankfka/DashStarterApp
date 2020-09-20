from typing import List

import pandas as pd

from config import Config, app_config
from models.OtherSampleDataItem import OtherSampleDataItem
from util import get_path

"""
This file holds the DataProvider class, which is responsible for the retrieval of data for the Dash application. If
required, the DataProvider is also responsible for the caching of retrieved data.
"""


class DataProvider:
    """
    Responsible for retrieval & update of all data for views
    """

    def __init__(self, config: Config):
        pass

    def get_sample_data_df(self) -> pd.DataFrame:
        return pd.read_csv(get_path('data/sample-data.csv'))

    def get_other_sample_data(self) -> List[OtherSampleDataItem]:
        return [
            OtherSampleDataItem.from_df_row(row)
            for idx, row in pd.read_csv(get_path('data/other-sample-data.csv')).iterrows()
        ]


# Instance of DataProvider that should be used in all views
app_data_provider: DataProvider = DataProvider(app_config)
