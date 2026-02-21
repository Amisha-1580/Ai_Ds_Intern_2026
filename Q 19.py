Q.19) Tuple unpacking: Loop over list of (x,y) coords, dict to count quadrant (if x>0,y>0 etc.).


# Program to count how many points are in each quadrant

# List of (x, y) coordinates
points = [(2, 3), (-1, 4), (-3, -2), (4, -5), (1, -1), (3, 2)]

# Dictionary to store quadrant counts
quadrants = {
    "Q1": 0,  # x > 0 and y > 0
    "Q2": 0,  # x < 0 and y > 0
    "Q3": 0,  # x < 0 and y < 0
    "Q4": 0   # x > 0 and y < 0
}

# Loop through the list of points
for (x, y) in points:   # tuple unpacking

    if x > 0 and y > 0:
        quadrants["Q1"] = quadrants["Q1"] + 1

    elif x < 0 and y > 0:
        quadrants["Q2"] = quadrants["Q2"] + 1

    elif x < 0 and y < 0:
        quadrants["Q3"] = quadrants["Q3"] + 1

    elif x > 0 and y < 0:
        quadrants["Q4"] = quadrants["Q4"] + 1

# Print the result
print("Points in each quadrant:")
for q, count in quadrants.items():
    print(q, ":", count)



OUTPUT: 

Points in each quadrant:
Q1 : 2
Q2 : 1
Q3 : 1
Q4 : 2
