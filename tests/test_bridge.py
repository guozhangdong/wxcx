import numpy as np
import pandas as pd
from prometheus_client import Gauge

import bridge


def test_bridge_cleans_dataframe():
    df = pd.DataFrame({"price": [1, np.nan], "other": [5, 6]})
    cols = ["price", "volume"]
    gauge = Gauge("test_nan_rate", "test")

    X, info = bridge.build_latest_feature_row(df, cols, nan_gauge=gauge, return_info=True)

    assert X.shape == (1, 2)
    assert X.dtype == np.float32
    assert info["missing_cols"] == ["volume"]
    assert gauge._value.get() == info["nan_rate"]
