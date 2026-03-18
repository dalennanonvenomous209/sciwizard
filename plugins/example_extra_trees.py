"""Example plugin: adds Extra Trees to the model catalogue.

Copy this file into your plugins/ directory and restart SciWizard.
Rename or duplicate it to add more models.

To use XGBoost instead, install it (pip install xgboost) and swap in:
    from xgboost import XGBClassifier
    registry["models"]["XGBoost"] = XGBClassifier(n_estimators=100, use_label_encoder=False)
"""

from sklearn.ensemble import ExtraTreesClassifier, ExtraTreesRegressor


def register(registry: dict) -> None:
    """Add Extra Trees (classification + regression) to SciWizard.

    Args:
        registry: The shared plugin registry with keys 'models' and 'preprocessors'.
    """
    registry["models"]["Extra Trees (Clf)"] = ExtraTreesClassifier(
        n_estimators=100, random_state=42
    )
    registry["models"]["Extra Trees (Reg)"] = ExtraTreesRegressor(
        n_estimators=100, random_state=42
    )
