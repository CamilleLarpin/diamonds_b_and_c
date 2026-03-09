# Decisions — diamonds_bc

> Load tier: cool
> Archive superseded decisions → DECISIONS_ARCHIVE.md

---

## [tooling] Ruff over flake8 + black
- **Decision**: Ruff handles both lint and format — no flake8, no black
- **Rationale**: single tool, faster, same rules; line-length 88 is black-compatible
- **Date**: 2026-03-09
- **Status**: active

## [tooling] Ignore N802/N803 in Ruff
- **Decision**: Uppercase `X`, `X_train`, `X_test` allowed; N802/N803 ignored globally
- **Rationale**: sklearn convention — feature matrix is always uppercase X; enforcing lowercase would make the code non-idiomatic
- **Date**: 2026-03-09
- **Status**: active

## [tooling] Exclude notebooks from Ruff
- **Decision**: `notebooks/` excluded from ruff scope
- **Rationale**: notebooks are scratch space (per CLAUDE.md) — style enforcement there adds friction with no value
- **Date**: 2026-03-09
- **Status**: active

## [git] Forked repo — push to fork remote
- **Decision**: always push branches to `fork` (CamilleLarpin/diamonds_b_and_c), never to `origin`
- **Rationale**: `origin` is vivadata/diamonds — upstream, read-only for contributors; PRs go fork → upstream
- **Date**: 2026-03-09
- **Status**: active
