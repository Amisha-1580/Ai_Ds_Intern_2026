Q.17) Nested dict {class: {student: grades}}; function to find class average using recursion-like loops


# Program to find average marks of each class
# using a nested dictionary and loops

# Nested dictionary: class -> student -> marks
school = {
    "Class A": {
        "Alice": 80,
        "Bob": 70,
        "Charlie": 90
    },
    "Class B": {
        "David": 60,
        "Emma": 75,
        "Frank": 85
    }
}

# Function to calculate class average
def class_average(data):
    # Loop through each class
    for class_name, students in data.items():
        total = 0
        count = 0

        # Loop through each student in the class
        for student, marks in students.items():
            total = total + marks
            count = count + 1

        # Calculate average for the class
        average = total / count
        print(class_name, "average is:", average)


OUTPUT :

Class A average is: 80.0
Class B average is: 73.33


class_average(school)
