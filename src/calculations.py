def calculate_fica_tax(annual_income, tax_data):
    ss_rate = tax_data["fica_rates"]["social_security"]["rate"]
    ss_limit = tax_data["fica_rates"]["social_security"]["income_limit"]
    medicare_rate = tax_data["fica_rates"]["medicare"]["rate"]
    medicare_tax = annual_income * medicare_rate
    taxable_ss_income = min(annual_income, ss_limit)
    ss_tax = taxable_ss_income * ss_rate
    fica_total = medicare_tax + ss_tax
    return {
        "social_security": round(ss_tax, 2),
        "medicare": round(medicare_tax, 2),
        "total": round(fica_total, 2),
    }


def calculate_federal_tax(taxable_income, filing_status, tax_data):
    brackets = tax_data["tax_brackets"][filing_status]
    total_tax = 0
    previous_cap = 0
    for bracket in brackets:
        income_cap = bracket["income_cap"]
        rate = bracket["rate"]
        if income_cap == "inf" or taxable_income <= income_cap:
            income_in_bracket = taxable_income - previous_cap
            total_tax += income_in_bracket * rate
            break
        else:
            income_in_bracket = income_cap - previous_cap
            total_tax += income_in_bracket * rate
            previous_cap = income_cap
    return {"federal_tax": round(total_tax, 2)}


def calculate_child_tax_credit(
    annual_income, filing_status, number_of_children, tax_data
):
    max_credit = (
        number_of_children
        * tax_data["tax_credits"]["child_tax_credit"]["amount_per_child"]
    )
    if (
        annual_income
        > tax_data["tax_credits"]["child_tax_credit"]["income_phaseout_thresholds"][
            filing_status
        ]
    ):
        max_credit = 0
    return {"child_tax_credit": max_credit}
