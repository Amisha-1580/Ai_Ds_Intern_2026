 Q 9) Function to reverse a list using a for loop and slicing; compare with tuples (immutable)


# Program to reverse a list and compare it with a tuple

# Function to reverse a list using a for loop
def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result


# Main part of the program
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Reverse list using function
print("Reversed list (for loop):", reverse_list(my_list))

# Reverse list using slicing
print("Reversed list (slicing):", my_list[::-1])

# Tuple example
my_tuple = (10, 20, 30, 40, 50)
print("\nOriginal tuple:", my_tuple)

# Reverse tuple using slicing
print("Reversed tuple:", my_tuple[::-1])

print("\nList can be changed (mutable), but tuple cannot be changed (immutable).")



OUTPUT :

Original list: [1, 2, 3, 4, 5]
Reversed list (for loop): [5, 4, 3, 2, 1]
Reversed list (slicing): [5, 4, 3, 2, 1]

Original tuple: (10, 20, 30, 40, 50)
Reversed tuple: (50, 40, 30, 20, 10)

List can be changed (mutable), but tuple cannot be changed (immutable).







