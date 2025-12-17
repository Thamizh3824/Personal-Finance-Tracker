Personal Finance Tracker (Python CLI):

    A modular, testable, CLI-based Personal Finance Tracker built in Python.
    Designed with clean architecture and open-source best practices in mind.

    This project allows users to record income and expenses, analyze financial data, and generate summaries and plots — all through a command-line interface.

✨ Key Features :

    •Add income and expense transactions via CLI
    •Store transactions in CSV format
    •Clean and validate financial data
    •Generate financial summaries:
        →Total income
        →Total expenses
        →Net savings
    •Generate expense/income plots
    •Modular architecture (loader, cleaner, analyzer, reporter, CLI)
    •Beginner-friendly pytest test suite

🏗️ Project Architecture:

Personal-Finance-Tracker/
├── finance_tracker/
│   ├── __init__.py
│   ├── analyzer.py      # Financial calculations
│   ├── cleaner.py       # Data validation & cleaning
│   ├── loader.py        # CSV loading
│   ├── reporter.py      # Reporting & plotting
│   ├── input_utils.py   # User input helpers
│   └── cli.py           # Command-line interface
├── tests/               # Pytest-based unit tests
├── finance_data.csv     # Sample data file
├── main.py              # Entry point
├── setup.cfg
├── pyproject.toml
└── README.md

🚀 Getting Started:

Prerequisites:
    •Python 3.9+
    •pip

Installation (Editable Mode):

    git clone https://github.com/Thamizh3824/Personal-Finance-Tracker.git
    cd Personal-Finance-Tracker
    pip install -e .

▶️ Running the Application:

    run:
        python main.py

    You will be presented with a CLI menu to:

        •Add transactions
        •View summaries
        •Generate plots

🧪 Running Tests:

    pytest

    All tests are written using pytest and focus on pure business logic.

🧠 Design Philosophy:

    This project follows open-source and production-ready principles:

        •Clear separation of concerns
        •No circular imports
        •Minimal logic in entry points
        •Testable, reusable modules
        •Safe incremental refactoring

    The architecture was intentionally designed to support:

        •Easy feature additions
        •Future database backends
        •Open-source contributions

🛣️ Future Improvements:

    •Database support (SQLite / PostgreSQL)
    •Monthly & category-wise analytics
    •Export reports as PDF
    •Budget alerts
    •Plugin-based data visualizations

🤝 Contributing:

    Contributions are welcome!

        1.Fork the repository
        2.Create a feature branch
        3.Add tests for your changes
        4.Submit a pull request

📄 License:

    MIT License