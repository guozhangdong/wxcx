"""Data fetcher module providing market data.

In absence of a real API, returns a mocked DataFrame with basic
price and volume information.
"""
from __future__ import annotations

import pandas as pd


def fetch_latest_data() -> pd.DataFrame:
    """Fetch the latest market data.

    Returns
    -------
    pd.DataFrame
        DataFrame containing at least ``price`` and ``volume`` columns.
    """
    # In real usage this would connect to a broker API. Here we simply return
    # a deterministic DataFrame for testing purposes.
    return pd.DataFrame([{"price": 1.0, "volume": 100.0}])
