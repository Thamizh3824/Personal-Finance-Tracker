import pandas as pd
from finance_tracker.loader import load_csv


def test_load_csv(tmp_path):
    file = tmp_path / "data.csv"

    df = pd.DataFrame(
        {
            "date": ["01-01-2024"],
            "amount": [1000],
            "category": ["Income"],
            "description": ["Salary"],
        }
    )
    df.to_csv(file, index=False)

    loaded_df = load_csv(file)
    assert not loaded_df.empty
    assert list(loaded_df.columns) == list(df.columns)

