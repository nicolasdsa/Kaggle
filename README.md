# Kaggle Lab

Repository for practicing statistical analysis, machine learning, and project organization in Python using Kaggle datasets and competitions.

## Goals

- study EDA, inference, and visualization without locking everything into notebooks
- standardize project structure to reduce repetition
- separate reusable code from dataset-specific code
- record learnings, metrics, and decisions in each project folder

## Structure

```text
.
├─ docs/
├─ projects/
│  └─ lego_database/
├─ src/
│  └─ kaggle_lab/
└─ tests/
```

- `src/kaggle_lab/common`: shared functions reused across projects
- `projects/<name>`: one dataset or problem per folder
- `projects/<name>/src`: pipeline specific to that problem
- `projects/<name>/notebooks`: guided exploration without concentrating all logic there
- `projects/<name>/configs`: experiment configurations
- `projects/<name>/artifacts`: generated models, predictions, and outputs

## Recommended Workflow

1. create a new project with `make new PROJECT=project_name`
2. document the goal, metric, and questions in the project's `README.md`
3. do EDA in notebooks and promote reusable logic into `src/`
4. consolidate a reproducible baseline via script and config
5. add minimal tests for critical transformations
6. record conclusions and next steps

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
make dev
```

If you use Kaggle credentials via `.env`, keep at least `KAGGLE_USERNAME` and `KAGGLE_KEY`.

## First Project

The initial project lives in [projects/lego_database](/home/nicolas/codigos/Kaggle/projects/lego_database) and uses the `rtatman/lego-database` dataset.

## Documentation

- [AGENTS.md](/home/nicolas/codigos/Kaggle/AGENTS.md)
- [docs/conventions.md](/home/nicolas/codigos/Kaggle/docs/conventions.md)
- [docs/roadmap.md](/home/nicolas/codigos/Kaggle/docs/roadmap.md)
