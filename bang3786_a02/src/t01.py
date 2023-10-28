"""
------------------------------------------------------------------------
Assignment 2, Task 1
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-07'
------------------------------------------------------------------------
"""

TAX_RATE = 18.5

total_sales = float(input("Enter total sales: $"))

tax_payable = total_sales * (TAX_RATE/100)

print(f"""
Projected Tax Report
{'-':-^26s}
Total Sales: ${total_sales:.2f}
Annual Tax:  %{TAX_RATE:.2f}
{'-':-^26s}
Tax:         ${tax_payable:.2f}
""")