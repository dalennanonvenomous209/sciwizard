# SciWizard Documentation

SciWizard is a desktop machine learning GUI. It lets you load data, preprocess it, train models, evaluate results, and make predictions — all without writing code.

---

## Quick navigation

| Guide | What's covered |
|-------|---------------|
| [Installation](installation.md) | System requirements, install steps, platform notes |
| [Usage](usage.md) | Step-by-step workflow walkthrough |
| [Architecture](architecture.md) | Code structure, layers, data flow |
| [Plugins](plugins.md) | Adding custom models and preprocessors |
| [Contributing](contributing.md) | Dev setup, standards, PR workflow |
| [FAQ](faq.md) | Common questions and troubleshooting |

---

## Design goals

- **No code required** for the common ML workflow — load → clean → train → evaluate → predict
- **No magic hidden from you** — every algorithm and parameter is visible and configurable
- **Extensible** — add models via the plugin system without touching core code
- **Fast** — heavy operations run in background threads; the UI stays responsive

---

## Supported algorithms

**Classification:** Logistic Regression, Random Forest, Gradient Boosting, Decision Tree, K-Nearest Neighbours, SVM (RBF), Naive Bayes

**Regression:** Linear Regression, Ridge, Random Forest, Gradient Boosting, Decision Tree, K-Nearest Neighbours, SVR

Custom algorithms can be added via plugins.
