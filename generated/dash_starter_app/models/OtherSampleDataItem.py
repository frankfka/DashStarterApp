from dataclasses import dataclass

from pandas import Series


"""
This file demonstrates the usage of a dataclass to abstract away data operations. Using dataclasses can be useful
for working with data where conversion from Dataframes or JSON is required.
"""


@dataclass
class OtherSampleDataItem:
    state: str
    total_exports: float
    beef_exports: float
    pork_exports: float
    poultry_exports: float
    dairy_exports: float

    @classmethod
    def from_df_row(cls, row: Series):
        return cls(
            state=row["state"],
            total_exports=row["total exports"],
            beef_exports=row["beef"],
            pork_exports=row["pork"],
            poultry_exports=row["poultry"],
            dairy_exports=row["dairy"]
        )
