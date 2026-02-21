Q.13) Use list comprehension with if to filter even numbers from 1-50 into a tuple.
  

  # Program to get even numbers from 1 to 50 using list comprehension

# Create a tuple of even numbers from 1 to 50
even_numbers = tuple([num for num in range(1, 51) if num % 2 == 0])

# Print the result
print("Even numbers from 1 to 50:")
print(even_numbers)


OUTPUT: 

Even numbers from 1 to 50:
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50)
