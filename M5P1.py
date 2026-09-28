# Get the quantity from the user
quantity = int(input("Enter the quantity: "))

# Determine the unit price
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

# Calculate extended price, tax, and total
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

# Display the results
print("\nOrder Summary")
print(f"Quantity:        {quantity}")
print(f"Unit Price:      ${unit_price:.2f}")
print(f"Extended Price:  ${extended_price:.2f}")
print(f"Tax (7%):        ${tax:.2f}")
print(f"Total:           ${total:.2f}")
