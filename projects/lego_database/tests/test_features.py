import pandas as pd

from projects.lego_database.src.features import build_set_level_dataset


def test_build_set_level_dataset_creates_expected_columns():
    tables = {
        "sets.csv": pd.DataFrame(
            {
                "set_num": ["A-1"],
                "name": ["Starter Set"],
                "year": [1999],
                "theme_id": [1],
                "num_parts": [42],
            }
        ),
        "themes.csv": pd.DataFrame({"id": [1], "name": ["Town"], "parent_id": [None]}),
        "inventories.csv": pd.DataFrame({"id": [10], "version": [1], "set_num": ["A-1"]}),
        "inventory_parts.csv": pd.DataFrame(
            {
                "inventory_id": [10, 10],
                "part_num": ["3001", "3002"],
                "color_id": [1, 5],
                "quantity": [10, 2],
            }
        ),
        "inventory_sets.csv": pd.DataFrame(),
        "parts.csv": pd.DataFrame(),
        "part_categories.csv": pd.DataFrame(),
        "colors.csv": pd.DataFrame(),
    }

    dataset = build_set_level_dataset(tables)

    assert "theme_depth" in dataset.columns
    assert "inventory_quantity" in dataset.columns
    assert dataset.loc[0, "complexity_class"] == "small"

