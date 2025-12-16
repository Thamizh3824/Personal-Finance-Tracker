import pandas as pd

REQUIRED_COLUMNS = {"date", "amount", "category", "description"}
DATE_FORMAT = "%d-%m-%Y"

def validate_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and clean transaction data.
    """
    validate_columns(df)

    df["date"] = pd.to_datetime(df["date"], format=DATE_FORMAT, errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["date", "amount"])
    return df
