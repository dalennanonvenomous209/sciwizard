"""Unit tests for ExperimentTracker."""

from __future__ import annotations

from pathlib import Path

import pytest
from sklearn.datasets import load_iris

from sciwizard.core.experiment_tracker import ExperimentTracker
from sciwizard.core.model_trainer import ModelTrainer


@pytest.fixture
def tracker(tmp_path: Path) -> ExperimentTracker:
    return ExperimentTracker(log_path=tmp_path / "experiments.jsonl")


@pytest.fixture
def result():
    data = load_iris(as_frame=True)
    trainer = ModelTrainer(task_type="classification", test_size=0.2, random_state=0)
    return trainer.train("Decision Tree", data.data, data.target)


def test_log_creates_file(tracker, result):
    tracker.log(result, dataset_name="iris")
    assert tracker._path.exists()


def test_load_history_returns_entries(tracker, result):
    tracker.log(result)
    tracker.log(result, notes="second run")
    history = tracker.load_history()
    assert len(history) == 2


def test_history_newest_first(tracker, result):
    tracker.log(result, notes="first")
    tracker.log(result, notes="second")
    history = tracker.load_history()
    assert history[0]["notes"] == "second"


def test_history_contains_correct_fields(tracker, result):
    tracker.log(result, dataset_name="test_ds", notes="my note")
    entry = tracker.load_history()[0]
    assert entry["model_name"] == "Decision Tree"
    assert entry["dataset"] == "test_ds"
    assert entry["task_type"] == "classification"
    assert "metrics" in entry
    assert entry["notes"] == "my note"


def test_clear_wipes_log(tracker, result):
    tracker.log(result)
    tracker.log(result)
    tracker.clear()
    assert tracker.load_history() == []


def test_empty_log_returns_empty_list(tracker):
    assert tracker.load_history() == []
