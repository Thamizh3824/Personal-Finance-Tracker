import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load transaction data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded transaction data
    """
    return pd.read_csv(file_path)

