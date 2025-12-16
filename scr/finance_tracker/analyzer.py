import pandas as pd

def total_income(df: pd.DataFrame) -> float:
    return df[df["category"] == "Income"]["amount"].sum()

def total_expense(df: pd.DataFrame) -> float:
    return df[df["category"] == "Expense"]["amount"].sum()

def net_savings(df: pd.DataFrame) -> float:
    return total_income(df) - total_expense(df)

