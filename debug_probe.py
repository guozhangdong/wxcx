"""Diagnostic tool for inspecting feature bridging."""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml
from prometheus_client import Gauge

import bridge
import data_fetcher

logger = logging.getLogger(__name__)


def run(config_path: str) -> None:
    with open(config_path, "r", encoding="utf-8") as f:
        config: dict[str, Any] = yaml.safe_load(f)
    cols = config["features"]["cols"]

    df = data_fetcher.fetch_latest_data()
    gauge = Gauge("features_nan_rate", "NaN rate of features")
    X, info = bridge.build_latest_feature_row(df, cols, nan_gauge=gauge, return_info=True)

    report = {
        "columns": cols,
        "dtype": info["dtype"],
        "shape": info["shape"],
        "missing_cols": info["missing_cols"],
        "nan_rate": info["nan_rate"],
    }

    np.save("debug_X.npy", X)
    with open("debug_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    logger.info(
        "missing=%s nan_rate=%.4f shape=%s dtype=%s",
        info["missing_cols"],
        info["nan_rate"],
        info["shape"],
        info["dtype"],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml", help="Config YAML path")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    run(args.config)


if __name__ == "__main__":
    main()
