# Architecture

SciWizard uses a layered MVC-style architecture with a strict dependency rule: `core` never imports from `ui`.

---

## Layer overview

```
┌─────────────────────────────────────┐
│           ui/  (PySide6)            │  Presentation — panels, widgets, theme
├─────────────────────────────────────┤
│           core/  (pure Python)      │  Business logic — data, training, registry
├─────────────────────────────────────┤
│  sklearn / pandas / numpy / joblib  │  Third-party scientific stack
└─────────────────────────────────────┘
```

Dependency rule: `core → third-party only`. `ui → core + PySide6 + matplotlib`.

---

## Package map

```
sciwizard/
├── app.py                  # Bootstrap: AppUserModelID, QApplication, MainWindow
├── config.py               # All constants and file paths in one place
│
├── core/
│   ├── data_manager.py     # DataManager — load, profile, clean, encode
│   ├── model_trainer.py    # ModelTrainer — train(), automl(); TrainingResult dataclass
│   ├── model_registry.py   # ModelRegistry — save/load/list/delete via joblib + JSON
│   ├── experiment_tracker.py  # ExperimentTracker — JSONL append/read/clear
│   └── plugin_loader.py    # PluginLoader — dynamic importlib discovery
│
└── ui/
    ├── main_window.py      # MainWindow — sidebar + QStackedWidget routing
    ├── theme.py            # QSS dark stylesheet + QPalette
    ├── workers.py          # Worker (QRunnable) + LongWorker (QThread)
    │
    ├── panels/
    │   ├── data_panel.py         # CSV load, preview, target selector, missing values
    │   ├── preprocessing_panel.py # Encoding, drop columns
    │   ├── viz_panel.py          # Matplotlib plots (histogram, scatter, heatmap, PCA)
    │   ├── training_panel.py     # Model config, threaded training, metric cards
    │   ├── automl_panel.py       # Leaderboard table, threaded AutoML sweep
    │   ├── eval_panel.py         # Confusion matrix, ROC, CV bar chart
    │   ├── prediction_panel.py   # Single form + batch CSV prediction
    │   ├── registry_panel.py     # List/load/delete registry entries
    │   └── experiments_panel.py  # Browse and clear experiment log
    │
    └── widgets/
        ├── common.py       # SectionHeader, MetricCard, PrimaryButton, StatusBadge, …
        └── plot_canvas.py  # PlotCanvas — FigureCanvas + NavToolbar in a QWidget
```

---

## Data flow

```
CSV file
   │
   ▼
DataManager.load_csv()
   │  stores _raw + _processed DataFrames
   │
   ├──► DataPanel  (preview, profile)
   ├──► PreprocessingPanel  (mutates _processed in-place)
   └──► VisualizationPanel  (reads _processed, renders Matplotlib)

DataManager.get_X_y()
   │
   ▼
ModelTrainer.train(model_name, X, y)
   │  runs in Worker (QRunnable, thread pool)
   │  returns TrainingResult
   │
   ├──► TrainingPanel  (metrics, CV log)
   ├──► EvaluationPanel  (confusion matrix, ROC, CV chart)
   ├──► PredictionPanel  (loads pipeline + feature_names)
   ├──► ModelRegistry.save()  →  ~/.sciwizard/models/<id>/
   └──► ExperimentTracker.log()  →  ~/.sciwizard/experiments.jsonl
```

---

## Threading model

All operations that could block — CSV loading is fast so done inline; training, AutoML, and batch prediction are always threaded:

| Operation | Worker type | Why |
|-----------|-------------|-----|
| Model training | `Worker` (QRunnable) | Thread-pool, fire and forget |
| AutoML sweep | `Worker` (QRunnable) | Same pool, progress via callback |
| Batch prediction | `Worker` (QRunnable) | May be large CSV |

`Worker` emits `signals.finished(result)` on success and `signals.error(exc, tb)` on failure. Panels connect to these signals. Qt's signal/slot mechanism is thread-safe — UI updates always happen on the main thread.

---

## Plugin system

`PluginLoader.load_all(registry)` scans `plugins/*.py` at startup. Each module must expose:

```python
def register(registry: dict) -> None:
    registry["models"]["My Model"] = MyEstimator()
    registry["preprocessors"]["My Step"] = MyTransformer()
```

The registry dict is passed into the training panel, which merges plugin models into its dropdown alongside the built-in catalogue.

---

## Model persistence format

```
~/.sciwizard/models/
└── <8-char uuid>/
    ├── model.joblib   — sklearn Pipeline (StandardScaler + estimator)
    └── meta.json      — model_id, alias, metrics, feature_names, saved_at, …
```

`joblib.dump` / `joblib.load` handles serialisation. `meta.json` is human-readable and can be queried without loading the pipeline.

---

## Config discipline

All magic strings, paths, and numeric defaults live in `config.py`. No panel or core module hardcodes a path or default value — they import from config. This makes the entire application reconfigurable from a single file.
