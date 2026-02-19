
Q .3) Create a list of 10 numbers, loop to find and print the maximum using only conditionals 
(no max()).


# Create a list of 10 numbers
numbers = [12, 45, 7, 89, 23, 56, 34, 90, 15, 60]

# Assume the first number in the list is the maximum
max_number = numbers[0]

# Loop through each number in the list
for num in numbers:

    # Compare current number with max_number
    if num > max_number:
        # If current number is greater, update max_number
        max_number = num

# Print the maximum number found
print("The maximum number in the list is:", max_number)


OUTPUT: 
The maximum number in the list is: 90
