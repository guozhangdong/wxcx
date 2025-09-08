"""Feature bridge ensuring model input consistency."""
from __future__ import annotations

import logging
from typing import Iterable, Tuple, Dict, Any

import numpy as np
import pandas as pd
from prometheus_client import Gauge

logger = logging.getLogger(__name__)


class FeatureBridgeError(RuntimeError):
    """Raised when the feature bridge cannot produce a valid input."""


def _coerce_numeric(row: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
    for col in cols:
        row[col] = pd.to_numeric(row[col], errors="coerce")
    return row


def build_latest_feature_row(
    df: pd.DataFrame,
    feature_cols: Iterable[str],
    *,
    nan_gauge: Gauge | None = None,
    return_info: bool = False,
) -> Tuple[np.ndarray, Dict[str, Any]] | np.ndarray:
    """Clean and align the latest feature row.

    Parameters
    ----------
    df : pd.DataFrame
        Source data frame.
    feature_cols : Iterable[str]
        Ordered list of required feature columns.
    nan_gauge : Gauge, optional
        Prometheus gauge to report NaN ratio.
    return_info : bool, default False
        Whether to return diagnostic information.

    Returns
    -------
    np.ndarray
        Array of shape ``(1, n)`` with ``float32`` dtype.
    dict, optional
        Diagnostic information if ``return_info`` is True.
    """
    if df.empty:
        raise FeatureBridgeError("input DataFrame is empty")

    cols = list(feature_cols)
    row = df.iloc[[-1]].copy()

    missing_cols = [c for c in cols if c not in row.columns]
    for col in missing_cols:
        row[col] = 0.0

    row = row[cols]
    row = _coerce_numeric(row, cols)
    row = row.replace([np.inf, -np.inf], np.nan)

    nan_mask = row.isna().to_numpy()
    nan_rate = float(nan_mask.sum() / nan_mask.size)
    if nan_gauge is not None:
        nan_gauge.set(nan_rate)

    if nan_rate > 0.0:
        logger.warning("NaN/inf detected in features: rate=%.4f", nan_rate)
        row = row.fillna(0.0)

    arr = row.to_numpy(dtype=np.float32, copy=False)

    info = {
        "missing_cols": missing_cols,
        "nan_rate": nan_rate,
        "shape": tuple(arr.shape),
        "dtype": str(arr.dtype),
    }

    if arr.shape != (1, len(cols)) or arr.dtype != np.float32:
        raise FeatureBridgeError(
            f"feature array invalid: missing={missing_cols}, nan_rate={nan_rate:.4f}, "
            f"shape={arr.shape}, dtype={arr.dtype}"
        )

    return (arr, info) if return_info else arr
