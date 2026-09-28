# Ask the user for the appliance name and cost
name = input("Enter the appliance name: ")
cost = float(input("Enter the cost of the appliance: $"))

# Determine the warranty cost
if cost > 1000:
    warranty = cost * 0.10
else:
    warranty = cost * 0.05

# Calculate the total cost
total = cost + warranty

# Display the results
print("Appliance Name:", name)
print("Appliance Cost: ${:.2f}".format(cost))
print("Warranty Cost: ${:.2f}".format(warranty))
print("Total Cost: ${:.2f}".format(total))