Q 5) Write a function that takes a list and returns a new list with only unique elements using a 
set


# creating Function to return unique elements
def unique_list(lst):
    # Convert list to set (removes duplicates)
    unique_values = set(lst)

    # Convert set back to list
    return list(unique_values)


# Main part of the program
numbers = [1, 2, 3, 2, 4, 1, 5]

print("Original list is:", numbers)

# Call the function
result = unique_list(numbers)

print("Unique elements are :", result)




OUTPUT : 

Original list is : [1, 2, 3, 2, 4, 1, 5]
Unique elements are : [1, 2, 3, 4, 5]

