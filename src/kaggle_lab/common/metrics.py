from __future__ import annotations

from dataclasses import dataclass

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


@dataclass(slots=True)
class RegressionReport:
    mae: float
    rmse: float
    r2: float


def regression_report(y_true, y_pred) -> RegressionReport:
    return RegressionReport(
        mae=float(mean_absolute_error(y_true, y_pred)),
        rmse=float(mean_squared_error(y_true, y_pred, squared=False)),
        r2=float(r2_score(y_true, y_pred)),
    )

