from sklearn.base import BaseEstimator, Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor

def create_model(model_name: str) -> BaseEstimator:
    """
    Create an untrained model with the best hyperparameters found during tuning.

    Parameters
    ----------
    model_name : str
        The name of the model (e.g. "ridge", "random_forest")

    Returns
    -------
    BaseEstimator
        The model ready to be fitted
    """
    BEST_PARAMS = {
    "ridge": {"alpha": 1.0},
    "random_forest": {"n_estimators": 200, "max_depth": 10, "random_state": 42},
    }
    
    if model_name == "ridge":
        return Ridge(**BEST_PARAMS["ridge"])

    elif model_name == "random_forest":
        return RandomForestRegressor(**BEST_PARAMS["random_forest"])

    else:
        raise ValueError(f"Unknown model name: {model_name}")   
           
    pass

def create_preproc() -> Pipeline:
    """
    Create a preprocessing pipeline.
    """
    pass

def train_model(model, X_train, y_train):
    pass

def evaluate_model(model, X_test, y_test) -> dict[str, float]:
    # NB : mae, mse, r2_score, mape
    # Only print the metrics for now
    pass

def predict(model, X):
    """
    Make predictions using the trained model.

    Parameters
    ----------
    model : any
        The trained model
    X : pd.DataFrame
        The raw data

    Returns
    -------
    pd.Series
        The predicted values
    """
    
