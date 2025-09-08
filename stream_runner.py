"""Simplified streaming runner that fetches data, bridges features and runs a model."""
from __future__ import annotations

import logging
from typing import Any

import yaml
from prometheus_client import Gauge, start_http_server

import bridge
import data_fetcher
import model_service

logger = logging.getLogger(__name__)


def run_once(config: dict[str, Any]) -> None:
    cols = config["features"]["cols"]
    gauge = Gauge("features_nan_rate", "NaN rate of features")

    df = data_fetcher.fetch_latest_data()
    if df.empty:
        logger.warning("data frame is empty before bridging")
        return

    try:
        X, info = bridge.build_latest_feature_row(df, cols, nan_gauge=gauge, return_info=True)
    except bridge.FeatureBridgeError as exc:
        logger.warning("bridge failed: %s", exc)
        raise

    logger.info("bridge output shape=%s dtype=%s", info["shape"], info["dtype"])

    model = model_service.load_model()
    proba = model_service.predict_proba_one(model, X[0])
    logger.info("prediction=%.4f", proba)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    start_http_server(8000)
    run_once(config)


if __name__ == "__main__":
    main()
