Q.12) Dictionary of {student: [grades]}; compute averages with loop, store in new dict, print top 3.


# Program to calculate average marks of students
# and print the top 3 students

# Dictionary with student names and their grades
students = {
    "Alice": [80, 90, 85],
    "Bob": [70, 75, 72],
    "Charlie": [95, 88, 92],
    "David": [60, 65, 70],
    "Emma": [85, 87, 90]
}

# Empty dictionary to store averages
averages = {}

# Calculate average for each student
for name, marks in students.items():
    total = 0
    for m in marks:
        total = total + m
    avg = total / len(marks)
    averages[name] = avg

print("Average marks of students:")
print(averages)

# Sorting  students by average marks (highest first)
sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 students:")

# Print only top 3 students
for i in range(3):
    print(sorted_students[i][0], "with average", sorted_students[i][1])


OUTPUT: 
Average marks of students:
{'Alice': 85.0, 'Bob': 72.33, 'Charlie': 91.67, 'David': 65.0, 'Emma': 87.33}

Top 3 students:
Charlie with average 91.67
Emma with average 87.33
Alice with average 85.0
