# Changelog

All notable changes to SciWizard are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2024-01-01

### Added

- **Data panel** — CSV loading, table preview (up to 500 rows), data profiling summary, missing value handling (drop, mean, median, mode fill, reset)
- **Preprocessing panel** — label encoding, one-hot encoding, column dropping
- **Visualization panel** — histogram, scatter plot, correlation heatmap, feature distributions, PCA 2D projection with class colouring
- **Training panel** — 7 classification algorithms, 7 regression algorithms, configurable train/test split, StandardScaler toggle, k-fold CV scores, threaded execution
- **AutoML panel** — automatic sweep of all catalogue models, sortable leaderboard, best model highlight
- **Evaluation panel** — confusion matrix with cell annotations, ROC curve (binary and multi-class OvR), cross-validation bar chart
- **Prediction panel** — form-based single-row prediction, batch CSV prediction with export
- **Model Registry** — joblib persistence, metadata JSON, alias support, list/load/delete UI
- **Experiment Tracker** — JSONL-backed run log, full metrics, CV stats, dataset name, notes; clearable from UI
- **Plugin system** — dynamic Python module loading from `/plugins` at startup; supports custom models and preprocessors
- **Dark theme** — Catppuccin-inspired stylesheet, custom Qt palette, embedded matplotlib dark style
- **Windows integration** — AppUserModelID via ctypes, taskbar icon from `icon/icon.ico`
- **Beginner mode toggle** — sidebar switch (foundation for future contextual help)
- **Non-blocking UI** — all training and batch operations run in `QRunnable`/`QThread` workers
- Full test suite covering `DataManager`, `ModelTrainer`, `ModelRegistry`, `ExperimentTracker`

---

## [Unreleased]

### Planned

- Hyperparameter grid search UI with `GridSearchCV`
- SHAP feature importance panel
- Export trained model as standalone Python script
- Light theme option
- Stratified k-fold toggle
- Import/export experiment history as CSV
