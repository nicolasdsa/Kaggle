# lego_database

Initial project based on the `rtatman/lego-database` dataset.

## Objective

Use a small, didactic relational dataset to practice:

- descriptive statistics and exploratory analysis
- joins, aggregations, and key validation
- feature engineering on relational tabular data
- regression to estimate `num_parts`
- classification to predict a set complexity band
- clustering and theme analysis from part and color profiles

## Dataset

This dataset usually includes these tables:

- `sets.csv`
- `themes.csv`
- `inventories.csv`
- `inventory_parts.csv`
- `inventory_sets.csv`
- `parts.csv`
- `part_categories.csv`
- `colors.csv`

## Statistical Analysis Questions

- How does the distribution of `num_parts` change across themes and over time?
- Which themes show the highest variability in set size?
- Does the color distribution vary systematically by theme?
- Is there a time trend in the average number of parts per set?
- Which part categories concentrate the most volume or diversity?
- Do older and newer themes have different complexity profiles?

## Machine Learning Possibilities

### Regression

- predict `num_parts` from `year`, `theme`, theme hierarchy depth, and inventory diversity

### Classification

- predict a complexity class (`small`, `medium`, `large`) from part and color aggregations
- predict the main theme of a set using category and color distributions

### Unsupervised

- cluster sets by part and color profile
- reduce dimensionality to visualize similarities between themes

## Suggested Roadmap

1. validate keys and join integrity
2. build an analytical dataset at set level
3. perform question-driven EDA
4. build a regression baseline for `num_parts`
5. try a simple complexity classification task
