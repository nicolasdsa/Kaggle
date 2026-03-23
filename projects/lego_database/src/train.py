from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

from kaggle_lab.common.metrics import regression_report
from kaggle_lab.common.preprocess import build_tabular_preprocessor
from kaggle_lab.common.splits import split_train_valid_test
from projects.lego_database.src.dataset import PROCESSED_DIR


def load_training_frame() -> pd.DataFrame:
    path = PROCESSED_DIR / "set_level_features.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Missing processed dataset: {path}. Run `python -m projects.lego_database.src.dataset build`."
        )
    return pd.read_csv(path)


def main() -> None:
    df = load_training_frame().dropna(subset=["num_parts"])
    feature_columns = [
        "year",
        "theme_name",
        "theme_depth",
        "inventory_count",
        "unique_parts",
        "unique_colors",
        "inventory_quantity",
    ]
    X = df[feature_columns]
    y = df["num_parts"]

    X_train, X_valid, X_test, y_train, y_valid, y_test = split_train_valid_test(X, y)
    preprocessor = build_tabular_preprocessor(X_train)
    regressor = RandomForestRegressor(
        n_estimators=300,
        max_depth=12,
        min_samples_leaf=2,
        n_jobs=-1,
        random_state=42,
    )
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", regressor),
        ]
    )

    model.fit(X_train, y_train)
    valid_pred = model.predict(X_valid)
    test_pred = model.predict(X_test)

    print("Validation:", regression_report(y_valid, valid_pred))
    print("Test:", regression_report(y_test, test_pred))
    print(f"Model trained using dataset at {Path(PROCESSED_DIR / 'set_level_features.csv')}")


if __name__ == "__main__":
    main()
