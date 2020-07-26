"""This module is responsible for loading benchmarks datasets."""

import pandas as pd

def load_temperatures() -> pd.DataFrame:
    """
    Loads daily-min-temperatures.csv.
    :return: Correspondent pandas dataframe
    """
    df_dataset = pd.read_csv("data/daily-min-temperatures.csv", index_col="index")

    return df_dataset

def load_births() -> pd.DataFrame:
    """
    Loads daily-total-female-births.csv.
    :return: Correspondent pandas dataframe
    """
    df_dataset = pd.read_csv("data/daily-total-female-births.csv", index_col="index")

    return df_dataset

def load_sunspots() -> pd.DataFrame:
    """
    Loads monthly-sunspots.csv.
    :return: Correspondent pandas dataframe
    """
    df_dataset = pd.read_csv("data/monthly-sunspots.csv", index_col="index")

    return df_dataset

def load_shampoo() -> pd.DataFrame:
    """
    Loads shampoo.csv.
    :return: Correspondent pandas dataframe
    """
    df_dataset = pd.read_csv("data/shampoo.csv", index_col="index")

    return df_dataset
