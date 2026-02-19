Q 8) Given list of scores, use while loop and conditionals to count passing (>=60) vs failing

# List of student scores
scores = [45, 78, 90, 30, 60, 55, 88]

# Initialize index and counters
i = 0
pass_count = 0
fail_count = 0

# Loop through the list using while loop
while i < len(scores):

    # Check if the score is passing if score is (60 or more)
    if scores[i] >= 60:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

    # Move to the next score
    i = i + 1

# Print the results here
print("Total passing students:", pass_count)
print("Total failing students:", fail_count)


OUTPUT:

Total passing students: 4
Total failing students: 3
