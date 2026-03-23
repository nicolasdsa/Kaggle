from __future__ import annotations

import argparse
from pathlib import Path

from kaggle_lab.common.io import ensure_dir


README_TEMPLATE = """# {project_name}

## Objective

Describe the problem, the main metric, and what you want to learn from this dataset.

## Dataset

Describe the source, the main tables, and the data granularity level.

## Statistical Analysis Questions

- What deserves descriptive analysis?
- Which distributions, correlations, or group comparisons are worth studying?
- Is there any statistical hypothesis worth testing?

## Machine Learning Possibilities

- Which target or task can be modeled?
- What baseline makes sense?
- Is there any leakage risk?

## Suggested Roadmap

1. validate schema and data quality
2. build a reproducible analytical dataset
3. perform question-driven EDA
4. build a simple baseline
5. record learnings and next steps
"""

BASELINE_CONFIG_TEMPLATE = """dataset_slug: ""
target: ""
random_state: 42
notes: "Fill this file with the project's baseline configuration."
model:
  type: ""
  params: {{}}
"""

NOTEBOOKS_README_TEMPLATE = """# Planned Notebooks

- `01_eda.ipynb`: initial exploration, data quality, and distributions
- `02_features.ipynb`: joins, transformations, and feature engineering
- `03_modeling.ipynb`: baseline, metrics, and comparisons

Promote any code that needs to be reproduced outside the notebook into `src/`.
"""

DATASET_TEMPLATE = '''from __future__ import annotations


def main() -> None:
    raise NotImplementedError("Implement ingestion and dataset assembly for this project.")


if __name__ == "__main__":
    main()
'''

FEATURES_TEMPLATE = '''from __future__ import annotations


def build_features():
    raise NotImplementedError("Implement feature engineering for this project.")
'''

TRAIN_TEMPLATE = '''from __future__ import annotations


def main() -> None:
    raise NotImplementedError("Implement the training baseline for this project.")


if __name__ == "__main__":
    main()
'''

TEST_TEMPLATE = '''def test_project_placeholder():
    """Replace this with a small deterministic test for the main transformation."""
    assert True
'''


def create_project(project_name: str) -> Path:
    project_dir = Path("projects") / project_name
    if project_dir.exists():
        raise FileExistsError(f"Project already exists: {project_dir}")

    directories = [
        project_dir / "configs",
        project_dir / "data" / "raw",
        project_dir / "data" / "interim",
        project_dir / "data" / "processed",
        project_dir / "notebooks",
        project_dir / "src",
        project_dir / "artifacts" / "models",
        project_dir / "artifacts" / "submissions",
        project_dir / "tests",
    ]

    for directory in directories:
        ensure_dir(directory)
        gitkeep = directory / ".gitkeep"
        gitkeep.touch(exist_ok=True)

    (project_dir / "README.md").write_text(
        README_TEMPLATE.format(project_name=project_name),
        encoding="utf-8",
    )
    (project_dir / "__init__.py").write_text(
        f'"""Project package for {project_name}."""\n',
        encoding="utf-8",
    )
    (project_dir / "configs" / "baseline.yaml").write_text(
        BASELINE_CONFIG_TEMPLATE,
        encoding="utf-8",
    )
    (project_dir / "notebooks" / "README.md").write_text(
        NOTEBOOKS_README_TEMPLATE,
        encoding="utf-8",
    )
    (project_dir / "src" / "__init__.py").write_text("", encoding="utf-8")
    (project_dir / "src" / "dataset.py").write_text(DATASET_TEMPLATE, encoding="utf-8")
    (project_dir / "src" / "features.py").write_text(FEATURES_TEMPLATE, encoding="utf-8")
    (project_dir / "src" / "train.py").write_text(TRAIN_TEMPLATE, encoding="utf-8")
    (project_dir / "tests" / "__init__.py").write_text("", encoding="utf-8")
    (project_dir / "tests" / "test_project.py").write_text(TEST_TEMPLATE, encoding="utf-8")
    return project_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new Kaggle study project.")
    parser.add_argument("project_name", help="Project folder name inside projects/.")
    args = parser.parse_args()
    project_dir = create_project(args.project_name)
    print(f"Created project at {project_dir}")


if __name__ == "__main__":
    main()
