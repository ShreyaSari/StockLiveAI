"""
Universal Dataset Loader

Author : Shreya Sari
Project : StockLiveAI
"""

from pathlib import Path
import pandas as pd

from preprocessing.schema import (
    COLUMN_MAPPING,
    MarketDataset,
)


class DataLoader:
    """
    Universal dataset loader.

    Supports:

    CSV

    Excel

    JSON

    Parquet
    """

    SUPPORTED_EXTENSIONS = {
        ".csv",
        ".xlsx",
        ".json",
        ".parquet",
    }

    def __init__(self):

        pass

    def load(self, filepath):

        filepath = Path(filepath)

        if not filepath.exists():
            raise FileNotFoundError(filepath)

        suffix = filepath.suffix.lower()

        if suffix not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type : {suffix}"
            )

        if suffix == ".csv":
            df = pd.read_csv(filepath)

        elif suffix == ".xlsx":
            df = pd.read_excel(filepath)

        elif suffix == ".json":
            df = pd.read_json(filepath)

        elif suffix == ".parquet":
            df = pd.read_parquet(filepath)

        else:
            raise ValueError(
                "Unknown format"
            )

        df = self._standardize_columns(df)

        dataset = MarketDataset(
            dataframe=df,
            source=str(filepath),
            rows=len(df),
            columns=len(df.columns),
            validated=False,
            cleaned=False,
        )

        return dataset

    def _standardize_columns(self, df):

        renamed = {}

        for column in df.columns:

            key = column.lower().strip()

            if key in COLUMN_MAPPING:

                renamed[column] = COLUMN_MAPPING[key]

        df = df.rename(columns=renamed)

        return df