# Ask the user for information
last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: $"))

# Calculate adjusted gross income
adjusted_gross_income = gross_income - (dependents * 12000)

# Determine the tax rate
if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

# Calculate income tax
income_tax = adjusted_gross_income * tax_rate

# If income tax is less than 0, set it to $100
if income_tax < 0:
    income_tax = 100.00

# Display the results
print("Last Name:", last_name)
print("Gross Income: ${:.2f}".format(gross_income))
print("Number of Dependents:", dependents)
print("Adjusted Gross Income: ${:.2f}".format(adjusted_gross_income))
print("Income Tax: ${:.2f}".format(income_tax))