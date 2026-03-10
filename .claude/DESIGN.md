# Design — diamonds_bc

> Load tier: cold

---

## Pipeline flow

```
load_data() → clean_data() → preprocess_data() → create_X_y()
                                                       ↓
                                              create_preproc() + create_model()
                                                       ↓
                                              train_model() → evaluate_model()
                                                       ↓
                                              save_model() / load_model()
```

## Module responsibilities

| Module | Responsibility |
|---|---|
| `data.py` | Load, clean, stateless transforms, X/y split |
| `model.py` | sklearn pipeline (preproc + model), train, evaluate, predict |
| `registry.py` | Save and load model artifacts (pickle) |
| `train.py` | End-to-end entrypoint — orchestrates all modules |

## Key constraints
- No external services or API calls
- sklearn ColumnTransformer (stateful) lives in `model.py` — saved with model artifact
- `preprocess_data` (data.py) handles stateless transforms only
