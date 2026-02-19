Q 4) Define a tuple of fruits; use a for loop to print those starting with 'A' or 'B'.


# Define a tuple of fruit names
fruits = ("Apple", "Banana", "Mango", "Orange", "Blueberry", "Grapes", "Avocado")

print("Fruits starting with 'A' or 'B':")

# Loop through each fruit in the tuple
for fruit in fruits:
    
    # Check if the fruit name starts with 'A' or 'B'
    if fruit[0] == "A" or fruit[0] == "B":
        print(fruit)


OUTPUT:

Fruits starting with 'A' or 'B':
Apple
Banana
Blueberry
Avocado
