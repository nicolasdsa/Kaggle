from __future__ import annotations

import pandas as pd


def build_theme_features(themes: pd.DataFrame) -> pd.DataFrame:
    theme_tree = themes[["id", "parent_id"]].copy()
    theme_tree["theme_depth"] = 0

    parent_lookup = themes.set_index("id")["parent_id"].to_dict()
    for theme_id in theme_tree["id"]:
        depth = 0
        current = parent_lookup.get(theme_id)
        while pd.notna(current):
            depth += 1
            current = parent_lookup.get(int(current))
        theme_tree.loc[theme_tree["id"] == theme_id, "theme_depth"] = depth

    return themes.merge(theme_tree[["id", "theme_depth"]], on="id", how="left")


def build_inventory_aggregates(
    inventories: pd.DataFrame,
    inventory_parts: pd.DataFrame,
) -> pd.DataFrame:
    parts_by_inventory = (
        inventory_parts.groupby("inventory_id")
        .agg(
            unique_parts=("part_num", "nunique"),
            unique_colors=("color_id", "nunique"),
            inventory_quantity=("quantity", "sum"),
        )
        .reset_index()
    )

    inventory_summary = inventories.merge(
        parts_by_inventory,
        left_on="id",
        right_on="inventory_id",
        how="left",
    )

    return (
        inventory_summary.groupby("set_num")
        .agg(
            inventory_count=("id", "nunique"),
            unique_parts=("unique_parts", "sum"),
            unique_colors=("unique_colors", "sum"),
            inventory_quantity=("inventory_quantity", "sum"),
        )
        .reset_index()
    )


def build_set_level_dataset(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    sets = tables["sets.csv"].copy()
    themes = build_theme_features(tables["themes.csv"].copy())
    inventories = tables["inventories.csv"].copy()
    inventory_parts = tables["inventory_parts.csv"].copy()

    inventory_summary = build_inventory_aggregates(inventories, inventory_parts)

    dataset = (
        sets.merge(themes, left_on="theme_id", right_on="id", how="left", suffixes=("", "_theme"))
        .merge(inventory_summary, on="set_num", how="left")
        .rename(columns={"name": "set_name", "name_theme": "theme_name"})
    )

    dataset["inventory_count"] = dataset["inventory_count"].fillna(0).astype(int)
    dataset["unique_parts"] = dataset["unique_parts"].fillna(0).astype(int)
    dataset["unique_colors"] = dataset["unique_colors"].fillna(0).astype(int)
    dataset["inventory_quantity"] = dataset["inventory_quantity"].fillna(0).astype(int)
    dataset["complexity_class"] = pd.cut(
        dataset["num_parts"],
        bins=[0, 100, 500, float("inf")],
        labels=["small", "medium", "large"],
        include_lowest=True,
    )
    return dataset

