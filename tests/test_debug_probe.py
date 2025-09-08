import json
from pathlib import Path

import pandas as pd

import data_fetcher
import debug_probe


def test_debug_probe_outputs(tmp_path, monkeypatch):
    config = tmp_path / "config.yaml"
    config.write_text("features:\n  cols: [price, volume]\n")

    def mock_fetch():
        return pd.DataFrame([{ "price": 1.0 }])

    monkeypatch.setattr(data_fetcher, "fetch_latest_data", mock_fetch)
    monkeypatch.chdir(tmp_path)

    debug_probe.run(str(config))

    assert (tmp_path / "debug_X.npy").exists()
    report = json.loads((tmp_path / "debug_report.json").read_text())
    assert "columns" in report and "nan_rate" in report
