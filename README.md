# U.S. Federal Tax Calculator (Python CLI)

## Project Overview

This project is a command-line interface (CLI) tool built in Python that provides an estimated annual federal tax liability for W-2 employees in the United States. The application was designed with a focus on accuracy, user-friendliness, and maintainability, serving as a practical tool for personal financial planning.

The core goal was to architect a robust application from the ground up, emphasizing clean code, separation of concerns, and thorough unit testing without relying on external libraries for the core logic.

## Key Features

* **Interactive User Input:** Guides the user through a series of clear, interactive prompts to gather all necessary information, including income, filing status, and common deductions.
* **Robust Input Validation:** Each user input function includes validation loops to handle incorrect data types (e.g., text instead of numbers) and invalid choices, re-prompting the user with helpful error messages.
* **Modular Architecture:** The application is organized into distinct modules for handling user input (`inputs.py`), performing tax calculations (`calculations.py`), and orchestrating the main application flow (`main.py`), demonstrating a professional separation of concerns.
* **Configuration-Based Tax Data:** All tax data (brackets, deductions, FICA rates, credits) is stored in an external `config.json` file. This makes the application highly maintainable, allowing for easy updates to tax information each year without changing any Python code.
* **Comprehensive Calculation Engine:**
  * Accurately calculates federal income tax based on the correct brackets for all standard filing statuses.
  * Correctly applies pre-tax deductions and the standard deduction to determine taxable income.
  * Calculates FICA (Social Security & Medicare) taxes, respecting the Social Security wage base limit.
  * Applies the Child Tax Credit, including income-based phase-out rules.
* **Detailed Reporting:** Generates a clean, formatted, and aligned report in the console, providing a full breakdown of the user's estimated tax liability.
* **Thorough Unit Testing:** The project is supported by a comprehensive test suite using Python's `unittest` and `unittest.mock` libraries to ensure the reliability of both the input validation and the calculation logic.

## How It Works

The application follows a clear, procedural workflow orchestrated by `main.py`:

1.  **Load Configuration:** The `config.json` file containing all tax data is loaded into a Python dictionary at startup.
2.  **Gather Inputs:** The user is guided through a series of prompts to provide their annual income (or hourly wage), filing status, pre-tax deductions, and number of dependents.
3.  **Calculate Taxable Income:** The script first calculates the user's total deductions and subtracts them from the gross annual income to determine the final taxable income.
4.  **Calculate Taxes & Credits:** The core calculation functions are called in the correct order:
    * FICA taxes are calculated based on gross income.
    * Federal income tax is calculated based on taxable income and the appropriate tax brackets.
    * The Child Tax Credit is calculated and subtracted from the federal tax liability.
5.  **Display Report:** A final, formatted report is printed to the console, summarizing all key figures for the user.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Navigate to the root directory of the project in your terminal.
3.  Run the main script:
    ```bash
    ./main.sh
    ```
4.  Follow the interactive prompts to enter your financial information.

## Disclaimer

This tool is for informational and educational purposes only and should not be considered a substitute for professional tax advice. The calculations are estimates based on the information provided and the tax rules defined in the `config.json` file.

---

*This project was built as part of the backend development curriculum on [Boot.dev](https://www.boot.dev).*
