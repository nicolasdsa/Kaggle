# AGENTS.md

This document defines the operational and architectural rules for agents and contributors who create or modify projects in this repository.

The goal of this repository is to practice statistical analysis and machine learning with Kaggle datasets without losing organization, reproducibility, or learning clarity.

## 1. Core Principle

Each dataset or problem must live in an isolated project inside `projects/`.

The repository is split into:

- `src/kaggle_lab/common`: utilities reused across projects
- `src/kaggle_lab/cli`: repository operational commands
- `projects/<project_slug>`: implementation specific to one dataset or problem

Main rule:

- generic code goes to `common`
- terminal automation goes to `cli`
- logic that knows dataset columns, joins, and rules goes to `projects/<project_slug>/src`

## 2. Required Structure For Each Project

Each new project must be created in `projects/<project_slug>/` with the minimum structure below:

```text
projects/<project_slug>/
├─ README.md
├─ __init__.py
├─ configs/
├─ data/
│  ├─ raw/
│  ├─ interim/
│  └─ processed/
├─ notebooks/
├─ src/
│  └─ __init__.py
├─ artifacts/
│  ├─ models/
│  └─ submissions/
└─ tests/
   └─ __init__.py
```

Empty folders should contain `.gitkeep` when preserving the structure is useful.

## 3. Responsibility Of Each Folder

### `README.md`

Every project must have its own `README.md` with:

- study goal
- short description of the dataset or problem
- statistical analysis questions
- machine learning possibilities
- suggested roadmap

The project `README` is not optional. It is part of the learning process.

### `configs/`

It should store experiment configuration in YAML.

Examples:

- target
- seed
- hyperparameters
- caminhos
- bins de classificacao

Rule:

- do not scatter magic values through the code if they can live in config

### `data/raw/`

Stores original data downloaded or copied from the source.

Rules:

- do not manually edit data in `raw`
- treat `raw` as read-only
- do not commit large or sensitive datasets

### `data/interim/`

Stores intermediate data, partial joins, or working tables.

Use it when a transformation is expensive or when inspecting an intermediate step is useful.

### `data/processed/`

Stores final datasets ready for structured EDA, training, or evaluation.

Rule:

- the content of `processed` must be reproducible from `raw` and code in `src`

### `notebooks/`

Used for exploration, EDA, quick tests, and iterative reasoning.

Rules:

- notebooks should be numbered: `01_eda`, `02_features`, `03_modeling`, etc.
- notebook explores; script reproduces
- any reused or important logic should be promoted into `src/`

### `src/`

Stores the reproducible pipeline for the project.

Expected files, when they make sense:

- `dataset.py`: ingestion, schema validation, dataset assembly
- `features.py`: feature engineering and main joins
- `train.py`: baseline training
- `predict.py`: inference or output generation
- `evaluate.py`: metrics and reports

Rule:

- `src/` is the source of truth for the pipeline
- notebooks should not replace the pipeline in `src/`

### `artifacts/models/`

Stores trained models, serialized artifacts, or checkpoints.

### `artifacts/submissions/`

Stores final predictions, submission CSV files, or equivalent outputs.

Rule for `artifacts/`:

- artifacts are generated outputs, not source code
- by default, do not commit heavy artifacts

### `tests/`

Stores project-specific tests.

Rules:

- test at least the most critical transformation
- prefer small and deterministic tests
- tests must not depend on the internet
- whenever possible, use minimal synthetic dataframes

## 4. Rules For `common`

`src/kaggle_lab/common` should stay small, generic, and predictable.

Move something into `common` only when:

- it has already been repeated in two or more projects
- the abstraction clearly reduces maintenance
- the function does not depend on columns or entities from a specific dataset

Do not move into `common`:

- dataset-specific joins
- features dependent on particular column names
- business logic from a single project

Examples that belong in `common`:

- file reading and writing
- generic column validation
- train, validation, and test splitting
- generic metrics
- generic tabular preprocessing

## 5. Rules For `cli`

`src/kaggle_lab/cli` should hold only repository operational commands.

Examples:

- create a new project
- validate structure
- trigger standard pipelines
- list existing projects

Rule:

- `cli` must not hold dataset-specific logic
- commands in `cli` orchestrate; business logic stays in project modules

## 6. Implementation Conventions

- folder and file names in `snake_case`
- prefer small functions with clear responsibility
- avoid a generic `utils.py` per project
- avoid giant notebooks with all logic mixed together
- prefer named constants over scattered strings
- fail early when expected schemas are incorrect

## 7. Learning Conventions

This repository does not exist only to produce models; it also exists to make reasoning explicit.

Therefore:

- each project should document questions and hypotheses
- the baseline should be simple before it becomes sophisticated
- EDA should come before heavy feature engineering
- advanced models should not appear before a reproducible baseline

## 8. Checklist For New Projects

When creating a new project, the agent must:

1. create the folder in `projects/<project_slug>`
2. add a `README.md` with goal, questions, and roadmap
3. create the `configs`, `data`, `notebooks`, `src`, `artifacts`, and `tests` structure
4. add at least one baseline configuration
5. create a data module if the project has structured ingestion
6. create at least one small test for the main transformation
7. ensure the structure respects the repository standard

## 9. What To Avoid

- abstracting too early
- moving project logic into `common` without need
- leaving all business logic in notebooks
- mixing raw data, processed data, and artifacts
- creating scripts without a clear role
- depending on scattered manual execution with no reproducible entrypoint

## 10. Final Rule

If there is doubt about where something should go:

- if it is generic and reusable, consider `common`
- if it is an operational command, consider `cli`
- if it knows the dataset deeply, keep it in the project

In case of a tie, prefer keeping the logic in the current project and only abstract after the repetition becomes real.
