def get_positive_float_input(prompt_text):
    while True:
        try:
            value = input(prompt_text)
            num = float(value)
            if num > 0:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g. 1234.56).")


def get_non_negative_int_input(prompt_text):
    while True:
        try:
            value = input(prompt_text)
            num = int(value)
            if num >= 0:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g. 1234)")


def get_salary_income():
    return get_positive_float_input("Please enter your annual salary: ")


def get_hourly_income():
    rate = get_positive_float_input("Please enter your hourly rate: ")
    hours = get_positive_float_input(
        "Please enter your average hours worked per week: "
    )
    while True:
        frequency = (
            input(
                "How often are you paid? Please enter one of the following:\n - 'w' for Weekly\n - 'bw' for Bi-Weekly\n - 'bm' for Bi-Monthly\n - 'm' for Monthly\nPay Frequency: "
            )
            .lower()
            .strip()
        )
        if frequency == "w":
            value = (rate * hours) * 52
        elif frequency == "bw":
            value = (rate * hours) * 26
        elif frequency == "bm":
            value = (rate * hours) * 24
        elif frequency == "m":
            value = ((rate * hours) * 52) / 12
        else:
            print("Invalid input Please enter 'w', 'bw', 'bm', or 'm'.")
            continue
        return round(value, 2)


def get_valid_income():
    while True:
        employee_type = (
            input(
                "Are you an hourly or salary employee?\nPlease enter 'h' for hourly or 's' for salary: "
            )
            .lower()
            .strip()
        )
        if employee_type == "h":
            return get_hourly_income()
        if employee_type == "s":
            return get_salary_income()
        print("Invalid input. Please enter 'h' or 's'.")


def get_valid_filing_status():
    while True:
        status = (
            input(
                "What is your filing status? Please enter one of the following:\n - 's' for Single\n - 'mj' for Married Filing Jointly\n - 'ms' for Married Filing Separately\n - 'w' for Qualifying Widow\nStatus: "
            )
            .lower()
            .strip()
        )
        if status == "s":
            return "single"
        elif status == "mj":
            return "married_filing_jointly"
        elif status == "ms":
            return "married_filing_separately"
        elif status == "w":
            return "qualifying_widow"
        print("Invalid input. Please enter 's', 'mj', 'ms', or 'w'.")


def get_investments_deductions():
    while True:
        status = (
            input(
                "Do you have any pre-tax investments? Please enter 'y' for yes and 'n' for no: "
            )
            .lower()
            .strip()
        )
        if status == "y":
            return get_positive_float_input(
                "How much do you contribute annually?\nPlease include the following contributions in your total:\n - 401k\n - Insurance Premiums\n - HSA/FSA\nAmount: "
            )
        elif status == "n":
            return 0
        print("Invalid input. Please enter 'y' or 'n'.")


def get_ira_deductions():
    while True:
        status = (
            input(
                "Do you contribute to a Traditional IRA? Please enter 'y' for yes or 'n' for no: "
            )
            .lower()
            .strip()
        )
        if status == "y":
            return get_positive_float_input(
                "How much do you contribute annually?\nAmount: "
            )
        elif status == "n":
            return 0
        print("Invalid input. Please enter 'y' or 'n'.")


def get_student_loan_interest():
    while True:
        status = (
            input(
                "Do you have a Student Loan? Please enter 'y' for yes or 'n' for no: "
            )
            .lower()
            .strip()
        )
        if status == "y":
            value = get_positive_float_input(
                "How much do you annually pay in interest?\nAmount: "
            )
            if value > 2500:
                return 2500
            return value
        elif status == "n":
            return 0
        print("Invalid input. Please enter 'y' or 'n'.")


def get_number_of_children():
    while True:
        status = (
            input("Do you have any children? Please enter 'y' for yes or 'n' for no: ")
            .lower()
            .strip()
        )
        if status == "y":
            return get_non_negative_int_input(
                "How many children do you have?\nAmount: "
            )
        if status == "n":
            return 0
        print("Invalid input. Please enter 'y' or 'n'.")
