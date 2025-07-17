import unittest

# Assuming your calculation functions are in 'src/calculations.py'
from src.calculations import (
    calculate_fica_tax,
    calculate_federal_tax,
    calculate_child_tax_credit,
)

# A mock tax_data dictionary for consistent testing
# This uses simplified 2024 data for clarity in tests
MOCK_TAX_DATA = {
    "tax_brackets": {
        "single": [
            {"rate": 0.10, "income_cap": 11600},
            {"rate": 0.12, "income_cap": 47150},
            {"rate": 0.22, "income_cap": "inf"},
        ],
        "married_filing_jointly": [
            {"rate": 0.10, "income_cap": 23200},
            {"rate": 0.12, "income_cap": 94300},
            {"rate": 0.22, "income_cap": "inf"},
        ],
    },
    "standard_deductions": {"single": 14600, "married_filing_jointly": 29200},
    "fica_rates": {
        "social_security": {"rate": 0.062, "income_limit": 168600},
        "medicare": {"rate": 0.0145},
    },
    "tax_credits": {
        "child_tax_credit": {
            "amount_per_child": 2000,
            "income_phaseout_thresholds": {
                "single": 200000,
                "married_filing_jointly": 400000,
            },
        }
    },
}


class TestCalculations(unittest.TestCase):

    def test_calculate_fica_tax_below_limit(self):
        # Tests FICA for an income below the Social Security limit
        income = 100000
        fica_result = calculate_fica_tax(income, MOCK_TAX_DATA)
        # Expected: (100000 * 0.062) + (100000 * 0.0145) = 6200 + 1450 = 7650
        self.assertEqual(fica_result["total"], 7650.0)
        self.assertEqual(fica_result["social_security"], 6200.0)
        self.assertEqual(fica_result["medicare"], 1450.0)

    def test_calculate_fica_tax_above_limit(self):
        # Tests FICA for an income above the Social Security limit
        income = 200000
        fica_result = calculate_fica_tax(income, MOCK_TAX_DATA)
        # Expected SS: 168600 * 0.062 = 10453.20
        # Expected Medicare: 200000 * 0.0145 = 2900.00
        # Total: 10453.20 + 2900.00 = 13353.20
        self.assertEqual(fica_result["total"], 13353.20)
        self.assertEqual(fica_result["social_security"], 10453.20)
        self.assertEqual(fica_result["medicare"], 2900.0)

    def test_calculate_federal_tax_single(self):
        # Tests federal tax for a single filer
        # Taxable income = 80000 - 14600 = 65400
        taxable_income = 65400
        tax_result = calculate_federal_tax(taxable_income, "single", MOCK_TAX_DATA)
        # Bracket 1: 11600 * 0.10 = 1160
        # Bracket 2: (47150 - 11600) * 0.12 = 35550 * 0.12 = 4266
        # Bracket 3: (65400 - 47150) * 0.22 = 18250 * 0.22 = 4015
        # Total: 1160 + 4266 + 4015 = 9441
        self.assertEqual(tax_result["federal_tax"], 9441.0)

    def test_calculate_federal_tax_married(self):
        # Tests federal tax for a married filing jointly filer
        # Taxable income = 150000 - 29200 = 120800
        taxable_income = 120800
        tax_result = calculate_federal_tax(
            taxable_income, "married_filing_jointly", MOCK_TAX_DATA
        )
        # Bracket 1: 23200 * 0.10 = 2320
        # Bracket 2: (94300 - 23200) * 0.12 = 71100 * 0.12 = 8532
        # Bracket 3: (120800 - 94300) * 0.22 = 26500 * 0.22 = 5830
        # Total: 2320 + 8532 + 5830 = 16682
        self.assertEqual(tax_result["federal_tax"], 16682.0)

    def test_child_tax_credit_full(self):
        # Tests the full child tax credit for an eligible income
        result = calculate_child_tax_credit(150000, "single", 2, MOCK_TAX_DATA)
        # 2 children * 2000/child = 4000
        self.assertEqual(result["child_tax_credit"], 4000)

    def test_child_tax_credit_phased_out(self):
        # Tests that the credit is 0 for an income above the threshold
        result = calculate_child_tax_credit(250000, "single", 2, MOCK_TAX_DATA)
        self.assertEqual(result["child_tax_credit"], 0)


if __name__ == "__main__":
    unittest.main()
