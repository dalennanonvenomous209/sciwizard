"""Input validation helpers shared across core and UI layers."""

from __future__ import annotations

from typing import Any

import pandas as pd


def require_dataframe(df: Any, label: str = "data") -> pd.DataFrame:
    """Assert that *df* is a non-empty DataFrame.

    Args:
        df: The object to validate.
        label: Name used in the error message.

    Returns:
        The original DataFrame if valid.

    Raises:
        ValueError: If *df* is None or empty.
    """
    if df is None:
        raise ValueError(f"{label} is None — load a dataset first.")
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"{label} must be a pandas DataFrame, got {type(df).__name__}")
    if df.empty:
        raise ValueError(f"{label} is empty.")
    return df


def require_column(df: pd.DataFrame, column: str) -> None:
    """Assert that *column* exists in *df*.

    Args:
        df: The DataFrame to check.
        column: Column name to look for.

    Raises:
        ValueError: If the column is not present.
    """
    if column not in df.columns:
        raise ValueError(
            f"Column '{column}' not found. Available columns: {list(df.columns)}"
        )


def require_numeric_columns(df: pd.DataFrame, columns: list[str]) -> None:
    """Assert that all listed columns are numeric.

    Args:
        df: The DataFrame to check.
        columns: Column names that must be numeric.

    Raises:
        ValueError: If any column is non-numeric.
    """
    non_numeric = [
        c for c in columns if c in df.columns and not pd.api.types.is_numeric_dtype(df[c])
    ]
    if non_numeric:
        raise ValueError(
            f"Columns must be numeric but are not: {non_numeric}. "
            "Use the Preprocess tab to encode them first."
        )


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp *value* between *lo* and *hi* (inclusive).

    Args:
        value: The value to clamp.
        lo: Lower bound.
        hi: Upper bound.

    Returns:
        Clamped value.
    """
    return max(lo, min(hi, value))


def truncate_str(s: str, max_len: int = 40, suffix: str = "…") -> str:
    """Truncate a string to *max_len* characters, appending *suffix* if trimmed.

    Args:
        s: Input string.
        max_len: Maximum allowed length including the suffix.
        suffix: String appended when truncation occurs.

    Returns:
        Original string if short enough, otherwise a truncated version.
    """
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix
