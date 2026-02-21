Q.18) Generate 20 random nums (1-100), use sets for uniques, dict for frequency, print most 
common with conditional.



# Program to generate random numbers and find the most common one

import random

# Generate 20 random numbers between 1 and 100
numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))

print("Random numbers:")
print(numbers)

# Use a set to find unique numbers
unique_numbers = set(numbers)
print("\nUnique numbers:")
print(unique_numbers)

# Create a dictionary to count frequency
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print("\nFrequency of each number:")
print(frequency)

# Find the most common number using conditionals
most_common = None
highest_count = 0

for num, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_common = num

print("\nMost common number is:", most_common)
print("It appeared", highest_count, "times")


OUTPUT:

Random numbers:
[12, 45, 12, 78, 45, 12, 90, 34, 78, 12, 56, 90, 45, 12, 67, 34, 12, 45, 23, 12]

Unique numbers:
{34, 67, 12, 45, 78, 23, 56, 90}

Frequency of each number:
{12: 7, 45: 4, 78: 2, 90: 2, 34: 2, 56: 1, 67: 1, 23: 1}

Most common number is: 12
It appeared 7 times
