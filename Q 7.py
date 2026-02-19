
Q 7) Create a dictionary of {name: age}; loop to print adults (>=18) using items()


# Create a dictionary with name as key and age as value
people = {
    "Alice": 22,
    "Bob": 15,
    "Charlie": 18,
    "David": 12,
    "Emma": 30
}

print("List of adults (age 18 or above):")

# Loop through dictionary using items()
for name, age in people.items():

    # Check if the person is an adult
    if age >= 18:
        print(name, "is", age, "years old")


OUTPUT: 

List of adults (age 18 or above):
Alice is 22 years old
Charlie is 18 years old
Emma is 30 years old
