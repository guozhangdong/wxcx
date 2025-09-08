"""Simplified model service used for demonstration and testing."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np


MODEL_FILE = Path("model.json")


def train_and_save(X: np.ndarray, y: np.ndarray) -> None:
    """Dummy training that stores the mean of labels."""
    model = {"bias": float(np.mean(y))}
    MODEL_FILE.write_text(json.dumps(model))


def load_model() -> dict[str, Any]:
    if MODEL_FILE.exists():
        return json.loads(MODEL_FILE.read_text())
    return {"bias": 0.0}


def predict_proba_one(model: dict[str, Any], x: np.ndarray) -> float:
    """Predict probability using a simple logistic function."""
    bias = model.get("bias", 0.0)
    score = float(np.sum(x) + bias)
    return float(1 / (1 + np.exp(-score)))
