import pandas as pd
import pytest
from finance_tracker.cleaner import clean_transactions


def test_clean_transactions_valid_data():
    df = pd.DataFrame(
        {
            "date": ["01-01-2024"],
            "amount": ["1000"],
            "category": ["Income"],
            "description": ["Salary"],
        }
    )

    cleaned = clean_transactions(df)
    assert not cleaned.empty
    assert cleaned["amount"].iloc[0] == 1000


def test_clean_transactions_missing_columns():
    df = pd.DataFrame({"date": ["01-01-2024"]})

    with pytest.raises(ValueError):
        clean_transactions(df)
