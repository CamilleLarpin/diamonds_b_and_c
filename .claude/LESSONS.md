# Lessons — diamonds_bc

> Load tier: cool
> NEVER delete entries. Split at 150 lines.

---

## [tooling] poetry lock required after editing pyproject.toml
> 2026-03-09
- Adding deps to `pyproject.toml` doesn't update `poetry.lock` automatically
- `poetry install` fails with "pyproject.toml changed significantly since lock file was last generated"
- Always run `poetry lock && poetry install` after editing dependencies

## [tooling] Ruff and pre-commit must be installed in the project virtualenv
> 2026-03-09
- `ruff` and `pre-commit` are not available globally via pyenv shims unless installed in the active virtualenv
- `make lint` and `pre-commit install` silently fail with "command not found"
- Install via `poetry install` (after `poetry lock`); or directly via the venv pip as a workaround

## [tooling] pre-commit only runs on staged files — make lint scans everything
> 2026-03-09
- `make lint` runs ruff on the entire project; pre-commit only checks files staged for commit
- Notebook lint errors surface in `make lint` but never in pre-commit unless the notebook is staged
- Exclude scratch directories (notebooks/) from ruff config to keep `make lint` clean
