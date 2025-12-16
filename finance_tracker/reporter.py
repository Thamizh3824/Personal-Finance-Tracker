import pandas as pd


def print_transactions(df: pd.DataFrame, start_date: str, end_date: str, date_format: str) -> None:
    print(f"Transactions from {start_date} to {end_date}")
    print(
        df.to_string(
            index=False,
            formatters={"date": lambda x: x.strftime(date_format)}
        )
    )


def print_summary(income: float, expense: float, savings: float) -> None:
    print("\nSummary:")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expense: ${expense:.2f}")
    print(f"Net Savings: ${savings:.2f}")
