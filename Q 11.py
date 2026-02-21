 Q 11)  Function: Input list of tuples (id, score); sort by score descending using sorted() and loop.


# Program to sort a list of (id, score) tuples by score in descending order

# Function to sort the list by score
def sort_by_score(data):
    # Use sorted() to sort by second value (score) in descending order
    sorted_list = sorted(data, key=lambda x: x[1], reverse=True)
    return sorted_list


# Main part of the program
students = [(1, 75), (2, 90), (3, 60), (4, 85)]

print("Original list:", students)

# Calling  the function
result = sort_by_score(students)

print("Sorted by score (highest to lowest):")

# Loop to print each tuple
for item in result:
    print(item)

OUTPUT : 
Original list: [(1, 75), (2, 90), (3, 60), (4, 85)]
Sorted by score (highest to lowest):
(2, 90)
(4, 85)
(1, 75)
(3, 60)
