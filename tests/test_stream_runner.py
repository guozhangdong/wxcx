import pandas as pd
from prometheus_client import CollectorRegistry, Gauge

import data_fetcher
import model_service
import stream_runner


def test_stream_runner(monkeypatch):
    config = {"features": {"cols": ["price", "volume"]}}

    registry = CollectorRegistry()
    monkeypatch.setattr(stream_runner, "Gauge", lambda *a, **k: Gauge(*a, registry=registry, **k))

    monkeypatch.setattr(data_fetcher, "fetch_latest_data", lambda: pd.DataFrame([{"price": 1.0, "volume": 2.0}]))
    monkeypatch.setattr(model_service, "load_model", lambda: {})
    monkeypatch.setattr(model_service, "predict_proba_one", lambda m, x: 0.5)

    stream_runner.run_once(config)

    assert registry.get_sample_value("features_nan_rate") == 0.0
