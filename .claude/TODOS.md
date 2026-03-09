# Todos — diamonds_bc

> CONTAINS: active milestones, next actions for this project.
> NOT HERE: decisions with rationale, completed and archived work.
> Keep it current — stale todos are noise.
> Load tier: warm

---

## Now — Séquence cible

### ~~1. Setup tooling~~ ✓ — PR open: `camille/setup-tooling`

### 2. Implémenter `data.py`
- [ ] `load_data()` — charger le CSV depuis `data/raw/` (ou seaborn fallback)
- [ ] `clean_data()` — supprimer doublons, gérer valeurs aberrantes (x/y/z = 0)
- [ ] `preprocess_data()` — encodage catégoriel (cut/color/clarity), scaling numérique
- [ ] `create_X_y()` — séparer features et target (`price`)
- [ ] Sauvegarder le dataset préprocessé dans `data/preprocessed/`

### 3. Implémenter `model.py`
- [ ] `create_preproc()` — pipeline sklearn (ColumnTransformer)
- [ ] `create_model()` — retourner le modèle sélectionné par `model_name`
- [ ] `train_model()` — fitter le modèle sure X_train, y_train
- [ ] `evaluate_model()` — calculer MAE, MSE, R², MAP ; logger les métriques (pas print)
- [ ] `predict()` — appliquer preproc + model sure données brutes

### 4. Implémenter `registry.py`
- [ ] `save_model()` — sérialiser avec joblib dans `models/`
- [ ] `load_model()` — désérialiser depuis `models/`

### 5. Implémenter `train.py`
- [ ] Brancher les étapes 2–4 dans `train()` (data → preproc → split → train → eval → save)
- [ ] Configurer `logging.basicConfig` au niveau INFO
- [ ] Vérifier : `python -m diamonds.train` fonctionne end-to-end

### 6. Tests
- [ ] `tests/test_data.py` — shape, types, absence de NaN après chaque étape
- [ ] `tests/test_model.py` — modèle fittable, predict retourne la bonne shape
- [ ] `tests/test_registry.py` — save → load → predict identique
- [ ] GitHub Actions CI — pytest sure chaque push

## Blocked
— aucun

## Done (recent — clear periodically)
- [x] Structure du package initialisée (`data.py`, `model.py`, `registry.py`, `train.py`, `params.py`)
- [x] Stubs + docstrings NumPy en place sure toutes les functions publiques
- [x] `data/raw/` et `models/` trackés dans git (`.gitkeep`)
- [x] Tooling setup — ruff, pre-commit, pytest, Makefile (PR: `camille/setup-tooling`)
