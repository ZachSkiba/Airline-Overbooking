import numpy as np
from scipy.integrate import quad

# Compensation Functions for Domestic and International Flights
def domestic_compensation(x, fare):
    """Domestic compensation based on delay time x."""
    if x < 1:
        return 0
    elif x < 2:
        return 2 * fare + 20 + 80 + 200  # 200% fare, $20 meal, $80 voucher, $200 flight
    elif x <= 6:
        return 4 * fare + 20 + 80 + 200  # 400% fare, $20 meal, $80 voucher, $200 flight
    return 0

def international_compensation(x, fare):
    """International compensation based on delay time x."""
    if x < 8:
        return 4 * fare + 20 + 80 + 600  # 400% fare, $20 meal, $80 voucher, $600 flight
    elif x < 12:
        return 4 * fare + 50 + 100 + 200 + 600  # 400% fare, $50 meal, $100 travel, $200 hotel, $600 flight
    elif x <= 24:
        return 4 * fare + 100 + 200 + 200 + 600  # 400% fare, $100 meal, $200 travel, $200 hotel, $600 flight
    return 0

# Triangular Distribution PDF and CDF
def triangular_pdf(x, a, b, c):
    """Probability density function (PDF) for triangular distribution."""
    if a <= x < b:
        return 2 * (x - a) / ((b - a) * (c - a))
    elif b <= x <= c:
        return 2 * (c - x) / ((c - b) * (c - a))
    return 0

# Integrate over the triangular distribution to calculate the expected compensation
def expected_compensation(compensation_function, a, b, c, fare):
    """Calculate the expected compensation using integration."""
    result, _ = quad(lambda x: compensation_function(x, fare) * triangular_pdf(x, a, b, c), a, c)
    return result

# Parameters
domestic_fare = 200  # Example domestic fare
international_fare = 600  # Example international fare

# Domestic flight parameters (min=1, mode=2, max=6)
a_domestic, b_domestic, c_domestic = 1, 2, 6

# International flight parameters (min=4, mode=8, max=24)
a_international, b_international, c_international = 4, 8, 24

# Calculate expected compensation for both domestic and international flights
expected_domestic = expected_compensation(domestic_compensation, a_domestic, b_domestic, c_domestic, domestic_fare)
expected_international = expected_compensation(international_compensation, a_international, b_international, c_international, international_fare)

print(f"Expected Domestic Compensation: ${expected_domestic:.2f}")
print(f"Expected International Compensation: ${expected_international:.2f}")
