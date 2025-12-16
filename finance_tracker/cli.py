from datetime import datetime

from finance_tracker.input_utils import (
    get_date,
    get_amount,
    get_category,
    get_description,
)

from finance_tracker.loader import load_csv
from finance_tracker.cleaner import clean_transactions
from finance_tracker.analyzer import total_income, total_expense, net_savings
from finance_tracker.reporter import print_transactions, print_summary
from finance_tracker.storage import CSV, plot_transactions

def run_cli():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            CSV.initialize_csv()
            date = get_date(
                "Enter the date of the transaction (dd-mm-yyyy) or press Enter for today: ",
                allow_default=True,
            )
            amount = get_amount()
            category = get_category()
            description = get_description()
            CSV.add_entry(date, amount, category, description)

        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")

            df = load_csv(CSV.CSV_FILE)
            df = clean_transactions(df)

            df["date"] = df["date"].dt.to_pydatetime()

            filtered_df = df[
                (df["date"] >= datetime.strptime(start_date, CSV.FORMAT))
                & (df["date"] <= datetime.strptime(end_date, CSV.FORMAT))
            ]

            if filtered_df.empty:
                print("No transactions found in the given date range.")
                continue

            income = total_income(filtered_df)
            expense = total_expense(filtered_df)
            savings = net_savings(filtered_df)

            print_transactions(
                filtered_df,
                start_date,
                end_date,
                CSV.FORMAT,
            )
            print_summary(income, expense, savings)

            if input("Do you want to see a plot? (y/n): ").lower() == "y":
                plot_transactions(filtered_df)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Enter a number between 1 and 3.")

