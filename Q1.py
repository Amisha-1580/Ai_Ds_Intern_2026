Q.1) Write a function using a while loop to print even numbers from 1 to 20.


# Function to print even numbers from 1 to 20
def print_even_numbers():
    # Start counting from 1
    number = 1

    # Loop will run until number becomes greater than 20
    while number <= 20:

        # Check if the number is even
        # Condition = A number is even if it is divisible by 2
        if number % 2 == 0:
            print(number)

        # Increase the number by 1 in each loop
        number = number + 1


# -------- Main Program Starts Here --------

print(" The Even numbers from 1 to 20 are:")

# Calling the function
print_even_numbers()


OUTPUT :

Even numbers from 1 to 20 are:
2
4
6
8
10
12
14
16
18
20


