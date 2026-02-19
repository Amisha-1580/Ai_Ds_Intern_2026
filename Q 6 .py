 Q 6) Use nested for loops and if to print a multiplication table (1-10) as a list of tuples.


# Create an empty list to store the tuples
box = []

# Outer loop for numbers from 1 to 10
for i in range(1, 11):

    # Inner loop for multiplying with numbers from 1 to 10
    for j in range(1, 11):

        # Multiply i and j
        result = i * j

        # Create a tuple (number, result)
        box.append((i, result))

# Print the final multiplication table
print("Multiplication box (as list of tuples):")
print(box)



OUTPUT : 

Multiplication box (as list of tuples):
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
 (2, 2), (2, 4), (2, 6), (2, 8), (2, 10), (2, 12), (2, 14), (2, 16), (2, 18), (2, 20),
 ...
 (10, 100)]
