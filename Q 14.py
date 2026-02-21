Q .14) Simulate shopping cart: list of dicts {item: price}; loop to apply 10% discount if total 
>100.


# Program to simulate a shopping cart and apply discount

# Shopping cart as a list of dictionaries
cart = [
    {"item": "Pen", "price": 20},
    {"item": "Book", "price": 50},
    {"item": "Bag", "price": 60}
]

total = 0

# Calculate total price
for product in cart:
    total = total + product["price"]

print("Total price before discount:", total)

# Apply 10% discount if total is more than 100
if total > 100:
    discount = total * 0.10
    total = total - discount
    print("Discount applied: 10%")
else:
    print("No discount applied")

print("Final price after discount:", total) 


OUTPIT : 

Total price before discount: 130
Discount applied: 10%
Final price after discount: 117.0

