"""Unit tests for the plugin loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from sciwizard.core.plugin_loader import PluginLoader


@pytest.fixture
def plugin_dir(tmp_path: Path) -> Path:
    return tmp_path / "plugins"


def _write_plugin(directory: Path, name: str, content: str) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    p = directory / name
    p.write_text(content)
    return p


def test_loads_valid_plugin(plugin_dir: Path):
    _write_plugin(plugin_dir, "my_model.py", """
from sklearn.dummy import DummyClassifier

def register(registry):
    registry["models"]["Dummy"] = DummyClassifier()
""")
    registry = {"models": {}, "preprocessors": {}}
    loader = PluginLoader(plugin_dir)
    loader.load_all(registry)
    assert "Dummy" in registry["models"]
    assert "my_model.py" in loader.loaded_plugins


def test_skips_underscore_files(plugin_dir: Path):
    _write_plugin(plugin_dir, "_internal.py", """
def register(registry):
    registry["models"]["Hidden"] = object()
""")
    registry = {"models": {}, "preprocessors": {}}
    PluginLoader(plugin_dir).load_all(registry)
    assert "Hidden" not in registry["models"]


def test_skips_plugin_without_register(plugin_dir: Path):
    _write_plugin(plugin_dir, "no_register.py", "x = 42\n")
    registry = {"models": {}, "preprocessors": {}}
    loader = PluginLoader(plugin_dir)
    loader.load_all(registry)
    assert "no_register.py" not in loader.loaded_plugins


def test_continues_after_broken_plugin(plugin_dir: Path):
    _write_plugin(plugin_dir, "broken.py", "raise RuntimeError('oops')\n")
    _write_plugin(plugin_dir, "good.py", """
def register(registry):
    registry["models"]["Good"] = object()
""")
    registry = {"models": {}, "preprocessors": {}}
    loader = PluginLoader(plugin_dir)
    loader.load_all(registry)
    assert "Good" in registry["models"]
    assert "good.py" in loader.loaded_plugins


def test_nonexistent_dir_is_silent():
    registry = {"models": {}, "preprocessors": {}}
    loader = PluginLoader(Path("/nonexistent/plugin/path"))
    loader.load_all(registry)  # must not raise
    assert registry["models"] == {}


def test_multiple_plugins(plugin_dir: Path):
    for i in range(3):
        _write_plugin(plugin_dir, f"model_{i}.py", f"""
def register(registry):
    registry["models"]["Model{i}"] = object()
""")
    registry = {"models": {}, "preprocessors": {}}
    PluginLoader(plugin_dir).load_all(registry)
    assert len(registry["models"]) == 3
