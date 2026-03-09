from sklearn.base import BaseEstimator, Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, ColumnTransformer, make_column_selector

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
    # categorical pipeline
    cat_pipe = Pipeline(
    [ ("cat_imp",SimpleImputer(strategy="most_frequent"))
      ,("ohe",OneHotEncoder(drop="first",sparse_output=False))
        ])
        
    # numerical pipeline
    num_pipe = Pipeline(
    [("knn_imp", KNNImputer(n_neighbors=5))
     ,("scaler", StandardScaler())
      ])
    
     # numerical and categorical pipeline
    preprocessor = ColumnTransformer(
    [("numeric",num_pipe, make_column_selector(dtype_include="number"))
    ,("categorical", cat_pipe, make_column_selector(dtype_exclude="number"))
      ]).set_output(transform="pandas")
    return preprocessor


def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
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
    
