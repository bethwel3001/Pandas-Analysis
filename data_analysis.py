import pandas as pd

def explore_dataset(df):
    """
    Explore the dataset by displaying the first few rows, data types, and missing values.
    Args:
        df (pd.DataFrame): The dataset to explore.
    """
    try:
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\nData types of each column:")
        print(df.dtypes)
        print("\nMissing values in each column:")
        print(df.isnull().sum())
    except Exception as e:
        print(f"Error during dataset exploration: {e}")

def clean_dataset(df):
    """
    Clean the dataset by filling or dropping missing values.
    Args:
        df (pd.DataFrame): The dataset to clean.
    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    try:
        if df.isnull().sum().sum() > 0:
            # For simplicity, drop rows with missing values
            df_clean = df.dropna()
            print(f"Dropped rows with missing values. New dataset shape: {df_clean.shape}")
            return df_clean
        else:
            print("No missing values found.")
            return df
    except Exception as e:
        print(f"Error during dataset cleaning: {e}")
        return df

def basic_statistics(df):
    """
    Compute basic statistics of numerical columns.
    Args:
        df (pd.DataFrame): The dataset.
    """
    try:
        print("Basic statistics of numerical columns:")
        print(df.describe())
    except Exception as e:
        print(f"Error computing basic statistics: {e}")

def group_by_category(df, category_col, numerical_col):
    """
    Perform grouping on a categorical column and compute mean of a numerical column.
    Args:
        df (pd.DataFrame): The dataset.
        category_col (str): The categorical column to group by.
        numerical_col (str): The numerical column to compute mean for.
    """
    try:
        grouped = df.groupby(category_col)[numerical_col].mean()
        print(f"Mean of {numerical_col} grouped by {category_col}:")
        print(grouped)
    except Exception as e:
        print(f"Error during grouping: {e}")
