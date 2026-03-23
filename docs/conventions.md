# Conventions

## Project Structure

- one project per dataset or competition inside `projects/`
- names in `snake_case`
- numbered notebooks: `01_eda`, `02_features`, `03_modeling`
- predictable scripts: `dataset.py`, `train.py`, `predict.py`, `evaluate.py`
- configurations in `configs/*.yaml`

## When To Move Something Into `common`

Promote code into `src/kaggle_lab/common` only when:

- it has already appeared in at least 2 projects
- the abstraction does not hide the learning logic
- the reuse clearly reduces maintenance

## Practical Rules

- notebook explores; script reproduces
- the project `README.md` records motivation, questions, and learnings
- datasets, models, and artifacts stay out of git
- each relevant experiment should have its own config
- tests should cover sensitive transformations, joins, and validations
