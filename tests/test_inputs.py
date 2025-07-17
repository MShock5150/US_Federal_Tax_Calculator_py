import unittest
from unittest.mock import patch

# Assuming your input functions are in a file named 'inputs.py'
from src.inputs import (
    get_positive_float_input,
    get_non_negative_int_input,
    get_salary_income,
    get_hourly_income,
    get_valid_income,
    get_investments_deductions,
    get_valid_filing_status,
    get_number_of_children,
)


class TestInputFunctions(unittest.TestCase):

    # The @patch decorator temporarily replaces a function in a specified
    # module with a mock object. Here, we replace the built-in 'input' function.
    # The 'side_effect' is a list of return values for consecutive calls
    # to the mocked input() function.
    @patch("builtins.input", side_effect=["abc", "-10", "50000.75"])
    def test_get_positive_float_input(self, mock_input):
        """
        Tests the generic helper for getting a positive float.
        It simulates the user entering text, then a negative number,
        then finally a valid positive number.
        """
        result = get_positive_float_input("Enter a float: ")
        self.assertEqual(result, 50000.75)

    @patch("builtins.input", side_effect=["-5", "two", "2"])
    def test_get_non_negative_int_input(self, mock_input):
        """
        Tests the generic helper for getting a non-negative integer.
        It simulates a negative number, then text, then a valid integer.
        """
        result = get_non_negative_int_input("Enter an int: ")
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["85000"])
    def test_get_salary_income(self, mock_input):
        """
        Tests the specific function for getting a salary.
        """
        result = get_salary_income()
        self.assertEqual(result, 85000.0)

    @patch("builtins.input", side_effect=["25.50", "40", "invalid", "bw"])
    def test_get_hourly_income(self, mock_input):
        """
        Tests the full workflow for getting hourly income, including
        an invalid frequency entry.
        """
        # (25.50 * 40) * 26 = 26520.0
        result = get_hourly_income()
        self.assertEqual(result, 26520.0)

    @patch("builtins.input", side_effect=["x", "h", "30", "35", "w"])
    def test_get_valid_income_hourly(self, mock_input):
        """
        Tests the main income orchestrator, simulating the user choosing 'hourly'.
        """
        # (30 * 35) * 52 = 54600.0
        result = get_valid_income()
        self.assertEqual(result, 54600.0)

    @patch("builtins.input", side_effect=["y", "19500"])
    def test_get_investments_deductions_yes(self, mock_input):
        """
        Tests the investment deduction function for a 'yes' answer.
        """
        result = get_investments_deductions()
        self.assertEqual(result, 19500.0)

    @patch("builtins.input", side_effect=["n"])
    def test_get_investments_deductions_no(self, mock_input):
        """
        Tests the investment deduction function for a 'no' answer.
        """
        result = get_investments_deductions()
        self.assertEqual(result, 0)

    @patch("builtins.input", side_effect=["single", "mj"])
    def test_get_valid_filing_status(self, mock_input):
        """
        Tests the filing status function, simulating an invalid entry
        followed by a valid one.
        """
        result = get_valid_filing_status()
        self.assertEqual(result, "married_filing_jointly")

    @patch("builtins.input", side_effect=["y", "3"])
    def test_get_number_of_children(self, mock_input):
        """
        Tests the children input function for a 'yes' answer.
        """
        result = get_number_of_children()
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
