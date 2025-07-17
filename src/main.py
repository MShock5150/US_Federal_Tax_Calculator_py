import json
from inputs import (
    get_valid_income,
    get_valid_filing_status,
    get_investments_deductions,
    get_ira_deductions,
    get_student_loan_interest,
    get_number_of_children,
)
from calculations import (
    calculate_fica_tax,
    calculate_federal_tax,
    calculate_child_tax_credit,
)


def load_tax_data(filepath):
    with open(filepath, "r") as config:
        return json.load(config)


def display_results(
    annual_income,
    taxable_income,
    liability_after_credit,
    fica_tax,
    total_tax,
):
    """
    Displays a formatted report of the tax calculation results to the console.
    """
    # --- Data for the report ---
    # We create a list of (label, value) tuples for easy processing
    report_lines = [
        ("Your Annual Income", annual_income),
        ("Your Taxable Income", taxable_income),
        ("Federal Tax Liability (after credits)", liability_after_credit),
        ("Social Security Tax", fica_tax["social_security"]),
        ("Medicare Tax", fica_tax["medicare"]),
        ("Total Estimated Tax Liability", total_tax),
    ]

    # --- Formatting for alignment ---
    # Find the length of the longest label to align all the values
    label_width = 0
    for label, _ in report_lines:
        if len(label) > label_width:
            label_width = len(label)

    # --- Build the report string ---
    header = "Based on the information you provided:"
    separator = "=" * (label_width + 20)  # Make the separator dynamic

    report = f"\n{header}\n{separator}\n"

    for label, value in report_lines:
        # The ':<{label_width}}' part left-aligns the label within the calculated width
        # The ':>15,.2f' part right-aligns the number and formats it as currency
        report += f"{label:<{label_width}} : ${value:>15,.2f}\n"

    report += f"{separator}\n"
    report += "Reminder: This is not legal tax advice, only an estimate.\n"
    report += "Please contact a CPA for a complete breakdown.\n"
    report += f"{separator}\n"
    report += "Thank you for using this software!\n"

    print(report)

    # Final prompt to exit
    while True:
        exit_cmd = input("Enter 'x' to exit the program: ").lower().strip()
        if exit_cmd == "x":
            break


def main():
    tax_data = load_tax_data("config.json")
    print(
        "Welcome! Let's calculate your estimated federal tax liability by answering a few questions."
    )
    annual_income = get_valid_income()
    filing_status = get_valid_filing_status()
    investment_deductions = get_investments_deductions()
    ira_deductions = get_ira_deductions()
    student_loan_interest = get_student_loan_interest()
    number_of_children = get_number_of_children()
    pre_tax_deductions = investment_deductions + ira_deductions + student_loan_interest
    standard_deduction = tax_data["standard_deductions"][filing_status]
    taxable_income = annual_income - (pre_tax_deductions + standard_deduction)
    if taxable_income < 0:
        taxable_income = 0
    fica_tax = calculate_fica_tax(annual_income, tax_data)
    federal_tax = calculate_federal_tax(taxable_income, filing_status, tax_data)
    child_tax_credit = calculate_child_tax_credit(
        annual_income,
        filing_status,
        number_of_children,
        tax_data,
    )
    liability_after_credit = (
        federal_tax["federal_tax"] - child_tax_credit["child_tax_credit"]
    )
    if liability_after_credit < 0:
        liability_after_credit = 0
    total_tax = liability_after_credit + fica_tax["total"]
    display_results(
        annual_income,
        taxable_income,
        liability_after_credit,
        fica_tax,
        total_tax,
    )


main()
