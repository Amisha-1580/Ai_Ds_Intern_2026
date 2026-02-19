 Q 10 ) Merge two sets of numbers; use intersection and union, print differences with loop



# Program to work with two sets of numbers

# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Find union (all elements from both sets)
union_set = set1 | set2
print("Union:", union_set)

# Find intersection (common elements)
intersection_set = set1 & set2
print("Intersection:", intersection_set)

print("\nElements only in set1:")
for item in set1:
    if item not in set2:
        print(item)

print("\nElements only in set2:")
for item in set2:
    if item not in set1:
        print(item)

OUTPUT:

Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}

Elements only in set1:
1
2

Elements only in set2:
5
6

