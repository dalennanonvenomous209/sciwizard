# FAQ

---

**Q: The app launches but the window is blank / all black.**

This is a Qt platform plugin issue on some Linux configurations. Try:

```bash
QT_QPA_PLATFORM=xcb python -m sciwizard
# or
QT_QPA_PLATFORM=wayland python -m sciwizard
```

Also ensure `libxcb-cursor0` and `libgl1` are installed (see [Installation](installation.md)).

---

**Q: My CSV loads but the column types look wrong (numbers shown as `object`).**

pandas infers types from content. If a numeric column contains stray text (e.g. `"N/A"` strings), it is read as `object`. Use the Preprocessing tab to drop or re-encode those columns, or clean the CSV externally before loading.

---

**Q: Training throws `ValueError: could not convert string to float`.**

Your feature matrix contains non-numeric columns that were not encoded. Go to the **Preprocess** tab and label-encode or one-hot encode the categorical columns before training.

---

**Q: The confusion matrix tab shows "classification only".**

Confusion matrices are only meaningful for classification. For regression tasks, use the CV Distribution tab to assess model quality.

---

**Q: ROC curve says "requires binary classification model with probability output".**

Some models (e.g. plain `SVC` without `probability=True`) do not expose `predict_proba`. SciWizard's built-in SVM catalogue entry has `probability=True` set. If you have added a custom model via a plugin without that flag, the ROC tab will be unavailable for that model.

---

**Q: Where are my saved models stored?**

`~/.sciwizard/models/` — one subdirectory per model, named by its 8-character ID. Each contains `model.joblib` and `meta.json`. You can copy these directories between machines.

---

**Q: Where is the experiment log?**

`~/.sciwizard/experiments.jsonl` — one JSON object per line, one line per run. Import it directly into pandas:

```python
import pandas as pd
df = pd.read_json("~/.sciwizard/experiments.jsonl", lines=True)
```

---

**Q: My plugin doesn't appear in the model list after I add it.**

- Make sure the file is in the `plugins/` directory at the project root
- The filename must not start with `_`
- The file must define `def register(registry: dict) -> None:`
- Restart SciWizard — plugins are loaded once at startup
- Check the console for a warning line mentioning your plugin filename

---

**Q: Can I use SciWizard with datasets that don't fit in memory?**

Not currently. SciWizard loads the entire CSV into a pandas DataFrame. For large datasets, sample your data externally first. Chunked loading is a planned future feature.

---

**Q: How do I reset all user data (models, experiments)?**

```bash
rm -rf ~/.sciwizard/
```

This removes all saved models and the experiment log. The app directory itself is unaffected.

---

**Q: Can I run SciWizard headlessly / in a script?**

The `core/` layer is fully independent of Qt and can be used as a library:

```python
from sciwizard.core.data_manager import DataManager
from sciwizard.core.model_trainer import ModelTrainer
from sciwizard.core.model_registry import ModelRegistry

dm = DataManager()
dm.load_csv("my_data.csv")
dm.target_column = "label"
dm.fill_missing_mean()

X, y = dm.get_X_y()
trainer = ModelTrainer(task_type="classification")
result = trainer.train("Random Forest", X, y)
print(result.metrics)

registry = ModelRegistry()
model_id = registry.save(result)
print("Saved as", model_id)
```
