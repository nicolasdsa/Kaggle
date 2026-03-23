import pandas as pd
import pytest

from kaggle_lab.common.validation import require_columns


def test_require_columns_raises_for_missing_columns():
    df = pd.DataFrame({"set_num": [1]})

    with pytest.raises(ValueError):
        require_columns(df, ["set_num", "name"], "sets")

