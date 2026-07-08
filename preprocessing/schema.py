"""
schema.py

Defines the standard schema used throughout StockLiveAI.

Every dataset—regardless of source—is converted into this format.

Author: Shreya Sari
Project: StockLiveAI
"""

from dataclasses import dataclass
from typing import Optional

import pandas as pd


# ----------------------------
# Required Columns
# ----------------------------

REQUIRED_COLUMNS = [
    "datetime",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "asset",
]


# ----------------------------
# Optional Columns
# ----------------------------

OPTIONAL_COLUMNS = [
    "market_cap",
    "fear_greed",
    "funding_rate",
    "open_interest",
    "sentiment",
]


# ----------------------------
# Automatic Column Mapping
# ----------------------------

COLUMN_MAPPING = {

    # Datetime
    "date": "datetime",
    "datetime": "datetime",
    "timestamp": "datetime",
    "time": "datetime",

    # Prices
    "open": "open",
    "o": "open",

    "high": "high",
    "h": "high",

    "low": "low",
    "l": "low",

    "close": "close",
    "c": "close",

    "volume": "volume",
    "vol": "volume",
    "v": "volume",

    # Asset
    "symbol": "asset",
    "coin": "asset",
    "asset": "asset",
}


@dataclass
class MarketDataset:
    """
    Standard object returned by the data pipeline.
    """

    dataframe: pd.DataFrame

    source: str

    rows: int

    columns: int

    validated: bool

    cleaned: bool