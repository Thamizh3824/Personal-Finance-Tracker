import pandas as pd
from finance_tracker.analyzer import total_income, total_expense, net_savings


def test_analyzer_calculations():
    df = pd.DataFrame(
        {
            "category": ["Income", "Expense", "Expense"],
            "amount": [2000, 500, 300],
        }
    )

    assert total_income(df) == 2000
    assert total_expense(df) == 800
    assert net_savings(df) == 1200

