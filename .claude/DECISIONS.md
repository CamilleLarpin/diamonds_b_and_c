# Decisions — diamonds_bc

> Load tier: cool
> Archive superseded decisions → DECISIONS_ARCHIVE.md

---

## [data] Data source: seaborn built-in dataset
- **Decision**: load via `sns.load_dataset("diamonds")` with CSV cache in `data/raw/`
- **Rationale**: dataset is built into seaborn (no external download needed); CSV cache avoids re-downloading on every run; `pd.read_csv` is faster than seaborn for repeated loads
- **Date**: 2026-03-09
- **Status**: active

## [data] clean_data: drop duplicates and zero-dimension rows only
- **Decision**: drop exact duplicates (146 rows) and rows where x/y/z == 0 (20 rows); keep outliers
- **Rationale**: duplicates confirmed as data entry errors (all 10 columns identical); zero dimensions are physically impossible; outliers (~5% at 1-99th pct) are real data — RandomForest is robust to them
- **Date**: 2026-03-09
- **Status**: active

## [data] preprocess_data: cast categoricals to category dtype
- **Decision**: cast `cut`, `color`, `clarity` to `category` dtype in `preprocess_data`
- **Rationale**: seaborn loads them as `category` but `pd.read_csv` (cache reload) returns `object`; `make_column_selector(dtype_exclude="number")` in the sklearn pipeline relies on `category` dtype — without this cast, the pipeline breaks on cached data
- **Date**: 2026-03-09
- **Status**: active

## [data] sklearn preprocessing stays in model.py
- **Decision**: imputation, scaling, OHE live in `create_preproc()` (model.py), not in `preprocess_data()` (data.py)
- **Rationale**: sklearn transformers are stateful (fitted on train data) — they must be saved and reused at predict time as part of the model artifact; `preprocess_data` handles only stateless, deterministic data-layer transforms
- **Date**: 2026-03-09
- **Status**: active

## [tooling] pre-commit: ruff + typos
- **Decision**: `.pre-commit-config.yaml` with ruff (lint + format) and typos (spell check)
- **Rationale**: fast, non-destructive hooks; ruff replaces flake8 + black in one tool; typos catches common misspellings without false positives
- **Date**: 2026-03-09
- **Status**: active
