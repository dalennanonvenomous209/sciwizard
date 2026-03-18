# SciWizard — Demo Dataset Walkthrough

This folder contains `customer_churn.csv` — a synthetic dataset of 500 telecom customers.
Use it to try every feature of SciWizard end to end.

---

## Dataset Overview

| Column | Type | Description |
|---|---|---|
| `customer_id` | Integer | Unique ID — drop this before training |
| `age` | Integer | Customer age (22–68) |
| `gender` | Categorical | Male / Female |
| `tenure_months` | Integer | Months as a customer (1–72) |
| `monthly_charges` | Float | Monthly bill amount ($20–$120) |
| `total_charges` | Float | Lifetime charges — has some missing values |
| `num_products` | Integer | Number of subscribed products (1–5) |
| `support_calls` | Integer | Support calls made — has some missing values |
| `satisfaction_score` | Integer | Self-reported score 1–10 |
| `internet_service` | Categorical | DSL / Fiber / None |
| `contract_type` | Categorical | Month-to-Month / One Year / Two Year |
| `payment_method` | Categorical | Credit Card / Bank Transfer / etc. |
| `churned` | **Target** | **Yes / No — predict this** |

- 500 rows, 13 columns
- ~29 missing values spread across `total_charges` and `support_calls`
- ~43% churn rate (Yes=214, No=286) — reasonable class balance

---

## Step 0 — Launch SciWizard

```bash
cd sciwizard          # the unzipped sciwizard folder
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m sciwizard
```

---

## Step 1 — Load the Data

1. Click **📊 Data** in the left sidebar
2. Click **📂 Load CSV**
3. Select `customer_churn.csv` from this `local/` folder
4. The table preview and profile panel populate immediately
5. In the **Target column** dropdown, select **`churned`**

You should see:
- **500 rows × 13 columns** in the header
- Profile panel on the right showing missing values in `total_charges` and `support_calls`

---

## Step 2 — Handle Missing Values

Still on the **Data** tab:

1. Click **Fill median** — this fills the numeric NaN cells with the column median
2. The profile panel updates; missing count should drop to 0
3. *(Optional)* Click **Reset** at any time to restore the original data and try a different strategy

---

## Step 3 — Preprocess

Click **🔧 Preprocess** in the sidebar.

**Encode categoricals** (models need numbers, not strings):

1. In the *Categorical Encoding* list, check:
   - `gender`
   - `internet_service`
   - `contract_type`
   - `payment_method`
2. Choose **Label Encode** from the method dropdown
3. Click **Apply Encoding**

**Drop the ID column** (it's not a feature):

1. In the *Columns to drop* list, check `customer_id`
2. Click **Drop selected columns**

The operations log at the bottom confirms each action.

---

## Step 4 — Explore the Data

Click **🎨 Visualize**.

Try these plots:

| Plot | X column | Y column | What to look for |
|---|---|---|---|
| Histogram | `monthly_charges` | — | Bimodal? Skewed? |
| Histogram | `satisfaction_score` | — | Distribution of scores |
| Scatter | `tenure_months` | `monthly_charges` | Any cluster pattern? |
| Correlation Heatmap | — | — | Which features correlate with each other? |
| PCA (2D) | — | — | Can the two classes be separated visually? |

---

## Step 5 — Train a Model

Click **🚀 Train**.

**Recommended first run:**

| Setting | Value |
|---|---|
| Task | Classification |
| Algorithm | Random Forest |
| Test size | 0.20 |
| Random seed | 42 |
| Scale features | ✅ checked |
| Save to registry | ✅ checked |
| Log to experiments | ✅ checked |

Click **🚀 Train**.

Training takes 1–3 seconds. You'll see metric cards appear:
- **Accuracy** — should be around 0.80–0.88
- **Precision, Recall, F1** — weighted averages across both classes

---

## Step 6 — Run AutoML

Click **⚡ AutoML**.

1. Set Task to **Classification**
2. Click **⚡ Run AutoML**

SciWizard tests all 7 classification algorithms and shows a ranked leaderboard.
Look for the best model — Gradient Boosting or Random Forest usually top this dataset.

---

## Step 7 — Evaluate

Click **📈 Evaluate** (auto-populated after Step 5).

- **Confusion Matrix** — see where the model confuses "Yes" and "No" churn
- **ROC Curve** — AUC above 0.85 is a solid result for this dataset
- **CV Distribution** — confirm the model is consistent across all 5 folds, not just lucky on one

---

## Step 8 — Tune Hyperparameters

Click **🔍 Hyperparams**.

1. Task: **Classification**, Model: **Random Forest**
2. The default grid searches `n_estimators`, `max_depth`, and `min_samples_split`
3. Click **🔍 Run Grid Search**
4. The leaderboard shows every parameter combination ranked by CV score
5. Note the best params — you can manually enter these on the Train tab for a final run

---

## Step 9 — Make a Prediction

Click **🔮 Predict**.

Fill in the form with a fictional customer, e.g.:

| Field | Value |
|---|---|
| age | 35 |
| gender | 1 (encoded Male=1 or Female=0 — check your encoding) |
| tenure_months | 6 |
| monthly_charges | 95 |
| total_charges | 570 |
| num_products | 1 |
| support_calls | 7 |
| satisfaction_score | 3 |
| internet_service | 1 (Fiber, likely label 1) |
| contract_type | 0 (Month-to-Month, likely label 0) |
| payment_method | 2 |

Click **Predict** — this customer profile (short tenure, high charges, low satisfaction, many support calls) should predict **Yes (churn)**.

**Batch prediction:**
1. Click **📂 Load CSV** in the Batch section
2. Load any CSV with the same column structure (minus `churned`)
3. Click **💾 Save Results** to export predictions

---

## Step 10 — Review History

Click **🧪 Experiments** to see every run from this session (and past sessions) with full metrics, CV scores, and timing.

Click **📦 Registry** to browse saved models. Select any row and click **📦 Load Selected** to restore that model to the Predict tab.

---

## Try Next

- Swap the target to `satisfaction_score` and run a **Regression** task
- Drop `churned` from features and predict `total_charges` instead
- Add your own model via a plugin in the `plugins/` folder
- Load your own real-world CSV and follow the same steps
