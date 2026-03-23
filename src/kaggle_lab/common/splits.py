from __future__ import annotations

from typing import Any

from sklearn.model_selection import train_test_split


def split_train_valid_test(
    X: Any,
    y: Any,
    *,
    test_size: float = 0.2,
    valid_size: float = 0.2,
    random_state: int = 42,
):
    X_train_valid, X_test, y_train_valid, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    valid_ratio = valid_size / (1 - test_size)
    X_train, X_valid, y_train, y_valid = train_test_split(
        X_train_valid,
        y_train_valid,
        test_size=valid_ratio,
        random_state=random_state,
    )
    return X_train, X_valid, X_test, y_train, y_valid, y_test
