# Usage Guide

Launch with:

```bash
python -m sciwizard
```

The window opens to the **Data** tab. Use the sidebar on the left to navigate between tabs.

---

## 1. Data Tab

**Load a CSV**

Click **Load CSV** and select a comma-separated file. SciWizard displays:

- Row and column counts in the header
- A table preview of up to 500 rows
- A profile panel on the right showing data types, row counts, and any missing values per column

**Select a target column**

Use the **Target column** dropdown to choose what you want to predict. This selection is used by the Train and AutoML tabs.

**Handle missing values**

| Button | Effect |
|--------|--------|
| Drop rows | Remove every row that contains at least one NaN |
| Fill mean | Replace numeric NaNs with the column mean |
| Fill median | Replace numeric NaNs with the column median |
| Fill mode | Replace all NaNs with the column mode |
| Reset | Restore the dataframe to its original loaded state |

---

## 2. Preprocess Tab

**Encode categorical columns**

Check one or more columns in the list, choose a method, and click **Apply Encoding**:

- *Label Encode* — replaces each unique string with an integer (0, 1, 2 …). Suitable for tree-based models.
- *One-Hot Encode* — creates binary indicator columns. Suitable for linear models.

**Drop columns**

Check columns you want to remove, then click **Drop selected columns**. This is useful for IDs, timestamps, or leaky features.

All operations are logged in the panel's log box. Use **Reset** on the Data tab to undo all preprocessing.

---

## 3. Visualize Tab

| Plot type | What it shows |
|-----------|--------------|
| Histogram | Distribution of a single numeric column |
| Scatter | Relationship between two numeric columns |
| Correlation Heatmap | Pairwise Pearson correlation of all numeric columns |
| Feature Distribution | Small multiples histogram for up to 9 columns |
| PCA (2D) | First two principal components; coloured by target if set |

Use the navigation toolbar (zoom, pan, save) embedded below each plot.

---

## 4. Train Tab

1. Select **Task type** — Classification or Regression
2. Pick an **Algorithm** from the dropdown
3. Set **Test size** (default 20%) and **Random seed**
4. Toggle **Scale features** to prepend a StandardScaler to the pipeline
5. Click **🚀 Train**

Training runs in a background thread — the UI stays responsive. When complete, you'll see:

- Metric cards (accuracy/F1 for classification, R²/MAE/RMSE for regression)
- Cross-validation scores (5-fold by default)
- Training duration

If **Save to registry** is checked, the model is automatically persisted. If **Log to experiment tracker** is checked, the run is appended to `~/.sciwizard/experiments.jsonl`.

---

## 5. AutoML Tab

Click **⚡ Run AutoML** to train every algorithm in the catalogue against the current dataset. The leaderboard shows all models sorted by score. The best model is highlighted at the bottom.

AutoML uses 5-fold cross-validation only — it does not persist any models. Once you identify the best algorithm, switch to the Train tab to train and save it properly.

---

## 6. Evaluate Tab

Populated automatically after training. Contains three sub-tabs:

- **Confusion Matrix** — classification only; cell values annotated
- **ROC Curve** — binary: single curve with AUC; multi-class: one-vs-rest curves per class
- **CV Distribution** — bar chart of per-fold CV scores with mean ± std band

---

## 7. Predict Tab

**Single prediction**

After training, the form is populated with one input field per feature. Enter values and click **Predict**. The result is displayed in large text below.

**Batch prediction**

Click **Load CSV** to upload an unlabelled dataset. SciWizard aligns columns by name, runs inference, and appends a `prediction` column. Click **Save Results** to export the annotated CSV.

---

## 8. Registry Tab

Lists all models saved to `~/.sciwizard/models/`. Columns show the model ID, alias, algorithm, task type, primary metric, CV mean, and save timestamp.

- **Load Selected** — loads the pipeline back into memory and updates the Predict tab
- **Delete Selected** — removes the model directory permanently after confirmation

---

## 9. Experiments Tab

Displays every training run logged during the session and from past sessions. Most recent runs appear first. Click **Clear Log** to wipe the history after confirming.
