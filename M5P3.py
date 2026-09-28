# Ask the user for the number of books and cost per book
num_books = int(input("Enter the number of books: "))
cost_per_book = float(input("Enter the cost per book: $"))

# Calculate the order total
order_total = num_books * cost_per_book

# Determine the shipping charge
if order_total > 50.00:
    shipping_charge = 0
else:
    shipping_charge = 25.00

# Display the results
print("Order Total: ${:.2f}".format(order_total))
print("Shipping Charge: ${:.2f}".format(shipping_charge))