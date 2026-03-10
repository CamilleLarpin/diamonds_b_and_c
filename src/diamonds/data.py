import os

import pandas as pd
import seaborn as sns
from loguru import logger

from diamonds.params import DATA_PATH

# Categorical columns: must be explicit — seaborn loads them as category dtype,
# but pd.read_csv (cache reload) loses that and returns object dtype instead.
CATEGORICAL_COLS = ["cut", "color", "clarity"]


def load_data(cache: bool = True) -> pd.DataFrame:
    """
    Load the diamonds dataset.

    Parameters
    ----------
    cache : bool, optional
        Whether to cache the dataset, by default True

    Returns
    -------
    pd.DataFrame
        The diamonds dataset
    """
    raw_path = os.path.join(DATA_PATH, "raw", "diamonds.csv")

    if cache and os.path.exists(raw_path):
        logger.info("Loading diamonds dataset from cache: {}", raw_path)
        return pd.read_csv(raw_path)

    # Source: seaborn built-in dataset (ggplot2 diamonds, 53940 rows)
    logger.info("Downloading diamonds dataset from seaborn")
    df = sns.load_dataset("diamonds")

    if cache:
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        df.to_csv(raw_path, index=False)
        logger.info("Cached dataset to {}", raw_path)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the diamonds dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The diamonds dataset

    Returns
    -------
    pd.DataFrame
        The cleaned diamonds dataset
    """
    initial_len = len(df)

    # Drop exact duplicates: all 10 columns identical → data entry errors
    df = df.drop_duplicates()
    logger.info("Dropped {} duplicate rows", initial_len - len(df))

    # Drop rows where x, y, or z is 0: physically impossible (dimension in mm)
    before_zero = len(df)
    df = df[(df[["x", "y", "z"]] != 0).all(axis=1)]
    logger.info("Dropped {} zero-dimension rows", before_zero - len(df))

    return df.reset_index(drop=True)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the diamonds dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned diamonds dataset

    Returns
    -------
    pd.DataFrame
        The preprocessed diamonds dataset
    """
    # Cast to category: ensures make_column_selector(dtype_exclude="number")
    # works correctly regardless of whether data came from seaborn or CSV cache
    df = df.copy()
    for col in CATEGORICAL_COLS:
        df[col] = df[col].astype("category")

    logger.debug(
        "preprocess_data: {} rows, dtypes corrected for {}", len(df), CATEGORICAL_COLS
    )
    return df


def create_X_y(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """
    Create the feature matrix X and target vector y from the diamonds dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The preprocessed diamonds dataset

    Returns
    -------
    (pd.DataFrame, pd.Series)
        The feature matrix X and target vector y
    """
    # Target is price; all other columns are features
    X = df.drop(columns=["price"])
    y = df["price"]
    logger.debug("X shape: {}, y shape: {}", X.shape, y.shape)
    return X, y


if __name__ == "__main__":
    df = load_data()
    df_clean = clean_data(df)
    df_preprocessed = preprocess_data(df_clean)
    X, y = create_X_y(df_preprocessed)
