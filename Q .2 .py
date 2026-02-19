
Q.2) Use if-elif-else to classify a number as positive, negative, or zero; test in a for loop over a 
list. 

# classify a number as positive, negative, or zero.
numbers = [10, -5, 0, 7, -2]

print("Number Classification Results is here:")

# Loop through each number in the list
for num in numbers:

    # Check if the number is greater than zero
    if num > 0:
        print(num, "is a Positive number")

    # Check if the number is less than zero
    elif num < 0:
        print(num, "is a Negative number")

    # If the number is neither positive nor negative, it must be zero
    else:
        print(num, "is Zero")


OUTPUT:

Number Classification Results is here:
10 is a Positive number
-5 is a Negative number
0 is Zero
7 is a Positive number
-2 is a Negative number
