# Lessons — diamonds_bc

> Load tier: cool
> NEVER delete entries.

---

## [git] Create feature branch before starting work
> 2026-03-09
- Started `data.py` work on `camille/setup-tooling` instead of a fresh `camille/data` branch
- Required a stash + branch switch + conflict resolution to fix
- Always: PR merged → `git fetch origin` → `git checkout -b <name>/<feature> origin/<base>` → work

## [git] Plan before build — execution gate
> 2026-03-09
- Jumped into implementing `data.py` without presenting a plan first
- Rule: >2 steps or touches external system → output numbered plan → wait for explicit approval
