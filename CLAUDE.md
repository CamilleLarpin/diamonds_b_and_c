@~/.claude/CLAUDE.md

# CLAUDE.md — diamonds_bc

## Project

Bootcamp project: refactor a Jupyter notebook into a production-ready Python ML package (`diamonds`).
Goal: predict diamond prices from raw features using scikit-learn.

**Stack**: Python 3.11 · pyenv-virtualenv · Poetry · scikit-learn · pandas · direnv

**Structure**:
```
src/diamonds/
  params.py     # constants and env vars
  data.py       # load / clean / preprocess / create_X_y
  model.py      # create_preproc / create_model / train_model / evaluate_model / predict
  registry.py   # save_model / load_model
  train.py      # end-to-end pipeline entrypoint
data/raw/       # source CSV (git-tracked, read-only)
data/preprocessed/
models/         # saved model artifacts (git-tracked)
notebooks/      # exploration only — never import from src
```

## Collaboration

Two contributors: **Camille** and **Boubachar**.

**Git workflow**:
- Never commit directly to `main`
- Always create a feature branch: `git checkout -b <name>/<feature>`
- Open a PR before merging — no self-merge without review

**Remotes** (forked repo):
- `fork` → `CamilleLarpin/diamonds_b_and_c` — push branches here (use SSH: `git@github.com:CamilleLarpin/diamonds_b_and_c.git`)
- `origin` → `vivadata/diamonds` — upstream, read-only
- Always push to `fork`: `git push -u fork <branch>`

## Code standards

### Linting & formatting — Ruff
- Ruff handles both lint and format (replaces flake8 + black)
- Config in `pyproject.toml` under `[tool.ruff]`
- Run: `ruff check . --fix && ruff format .`
- Never leave unused imports or undefined names

### Pre-commit
- Hooks: `ruff` (lint + format) + `typos` (spelling) — fast, non-destructive
- Install once: `pre-commit install`
- Scope: pre-commit never runs `train.py` or anything that modifies data/models

### Logging
- Use `logging` (stdlib), never `print()` in `src/`
- Logger per module: `logger = logging.getLogger(__name__)`
- Level convention: DEBUG for intermediate values, INFO for pipeline steps, WARNING for recoverable issues
- `train.py` configures root logger at INFO: `logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s — %(message)s")`

### Documentation
- All public functions have docstrings (NumPy style — already in stubs)
- Params and return types annotated
- `notebooks/` is scratch space — no docstrings required there

## Environment

- Local: pyenv-virtualenv `diamonds` + direnv (`.envrc` committed, `.env` gitignored)
- `MODEL_REGISTRY` env var controls where models are saved (`local` default)
- Never hardcode paths — use `params.py` constants

## Makefile targets

```makefile
lint:
    ruff check . --fix && ruff format .

train:
    python -m diamonds.train

test:
    pytest src/tests/
```

## Constraints

- No external services, no API calls — this is a local ML pipeline
- `data/` and `models/` are git-tracked (small files); never commit credentials
- Notebook is for exploration only — all reusable logic goes in `src/`
