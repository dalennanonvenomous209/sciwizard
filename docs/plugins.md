# Plugin System

SciWizard discovers Python files in the `plugins/` directory at startup and calls their `register()` function to extend the model and preprocessor catalogues — no changes to core code needed.

---

## How it works

1. On launch, `PluginLoader.load_all(registry)` walks `plugins/*.py`
2. Each file is imported as a module via `importlib`
3. If the module has a `register(registry)` function, it is called
4. The registry dict is then available to panels at startup

Files starting with `_` are skipped (use `_scratch.py` for experiments).

---

## The registry dict

```python
registry = {
    "models": {},        # dict[str, sklearn-compatible estimator]
    "preprocessors": {}, # dict[str, sklearn Transformer]
}
```

Anything you add to `registry["models"]` appears in the **Train** tab's algorithm dropdown, labelled by its key.

---

## Writing a model plugin

```python
# plugins/extra_trees.py
from sklearn.ensemble import ExtraTreesClassifier

def register(registry: dict) -> None:
    registry["models"]["Extra Trees"] = ExtraTreesClassifier(
        n_estimators=200,
        random_state=42,
    )
```

That's it. Restart SciWizard and "Extra Trees" appears in the model selector.

---

## Writing a preprocessor plugin

Preprocessors are not yet wired into the UI directly, but you can add them to the registry for use in custom pipelines or future panels:

```python
# plugins/power_transformer.py
from sklearn.preprocessing import PowerTransformer

def register(registry: dict) -> None:
    registry["preprocessors"]["Yeo-Johnson"] = PowerTransformer(method="yeo-johnson")
```

---

## Multi-model plugin

```python
# plugins/boosting_suite.py
from sklearn.ensemble import AdaBoostClassifier, HistGradientBoostingClassifier

def register(registry: dict) -> None:
    registry["models"]["AdaBoost"] = AdaBoostClassifier(n_estimators=100)
    registry["models"]["HistGradientBoosting"] = HistGradientBoostingClassifier()
```

---

## Error handling

If a plugin raises any exception during loading, SciWizard logs a warning and continues — broken plugins do not crash the application.

Check the console or your log output for messages like:

```
WARNING sciwizard.core.plugin_loader — Failed to load plugin my_plugin.py: ImportError: No module named 'xgboost'
```

---

## Plugin directory location

By default: `<project root>/plugins/`

Override in code:

```python
PluginLoader(plugin_dir=Path("/custom/path/plugins")).load_all(registry)
```

---

## Security note

Plugins are executed as arbitrary Python code with the same privileges as the main process. Only load plugins from sources you trust. See [SECURITY.md](../SECURITY.md).
