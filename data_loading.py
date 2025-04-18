import pandas as pd
from sklearn.datasets import load_iris

def load_iris_dataset():
    """
    Load the Iris dataset from sklearn and convert it to a pandas DataFrame.
    Returns:
        df (pd.DataFrame): DataFrame containing the Iris dataset features and target.
    """
    try:
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['target'] = iris.target
        return df
    except Exception as e:
        print(f"Error loading Iris dataset: {e}")
        return None
