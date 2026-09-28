# Ask the user for the item and quantity
item = input("Enter item (A or B): ")
quantity = int(input("Enter quantity: "))

# Determine the unit price
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

# Calculate the extended price
extended_price = quantity * unit_price

# Display the results
print("Item:", item)
print("Unit Price: ${:.2f}".format(unit_price))
print("Extended Price: ${:.2f}".format(extended_price))