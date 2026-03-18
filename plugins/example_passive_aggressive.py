"""Example plugin: SGDClassifier (replaces deprecated PassiveAggressiveClassifier)
and a Normalizer preprocessor.
"""

from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import Normalizer


def register(registry: dict) -> None:
    """Register plugin components.

    Args:
        registry: SciWizard plugin registry with 'models' and 'preprocessors' keys.
    """
    # SGDClassifier with PA-I update rule — equivalent to PassiveAggressiveClassifier
    registry["models"]["SGD (PA-I)"] = SGDClassifier(
        loss="hinge",
        penalty=None,
        learning_rate="pa1",
        eta0=1.0,
        max_iter=1000,
        random_state=42,
    )
    registry["preprocessors"]["Normalizer (L2)"] = Normalizer(norm="l2")
