"""
validator.py

Validates market datasets before they enter the pipeline.

Author: Shreya Sari
Project: StockLiveAI
"""

from dataclasses import dataclass, field
from typing import List

import pandas as pd

from preprocessing.schema import REQUIRED_COLUMNS, MarketDataset


@dataclass
class ValidationReport:
    """
    Stores the results of dataset validation.
    """

    passed: bool = True
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class DataValidator:
    """
    Validates datasets against the StockLiveAI schema.
    """

    def validate(self, dataset: MarketDataset) -> ValidationReport:

        report = ValidationReport()

        df = dataset.dataframe

        # -------------------------
        # Required columns
        # -------------------------

        for column in REQUIRED_COLUMNS:

            if column not in df.columns:
                report.errors.append(
                    f"Missing required column: {column}"
                )

        # -------------------------
        # Missing Values
        # -------------------------

        missing = df.isnull().sum()

        for column, count in missing.items():

            if count > 0:
                report.warnings.append(
                    f"{column} contains {count} missing values."
                )

        # -------------------------
        # Duplicate Rows
        # -------------------------

        duplicates = df.duplicated().sum()

        if duplicates > 0:
            report.warnings.append(
                f"Dataset contains {duplicates} duplicate rows."
            )

        # -------------------------
        # Negative Prices
        # -------------------------

        price_columns = [
            "open",
            "high",
            "low",
            "close",
        ]

        for column in price_columns:

            if column in df.columns:

                if (df[column] < 0).any():

                    report.errors.append(
                        f"{column} contains negative values."
                    )

        # -------------------------
        # Negative Volume
        # -------------------------

        if "volume" in df.columns:

            if (df["volume"] < 0).any():

                report.errors.append(
                    "Volume contains negative values."
                )

        # -------------------------
        # Datetime Check
        # -------------------------

        if "datetime" in df.columns:

            try:

                pd.to_datetime(df["datetime"])

            except Exception:

                report.errors.append(
                    "Datetime column cannot be parsed."
                )

        # -------------------------
        # Chronological Order
        # -------------------------

        if "datetime" in df.columns:

            dates = pd.to_datetime(df["datetime"])

            if not dates.is_monotonic_increasing:

                report.warnings.append(
                    "Dataset is not sorted chronologically."
                )

        report.passed = len(report.errors) == 0

        return report