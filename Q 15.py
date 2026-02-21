Q.15) Function to remove duplicates from list of dicts by key 'id' using set of ids


# Program to remove duplicate records based on 'id'

# Function to remove duplicates using a set
def remove_duplicates(data):
    unique_data = []     # this will store final result
    seen_ids = set()     # this will store ids we have already seen

    # Loop through each dictionary in the list
    for item in data:
        # Check if this id is already in seen_ids
        if item["id"] not in seen_ids:
            unique_data.append(item)      # add item to result list
            seen_ids.add(item["id"])      # add id to set

    return unique_data


# -------- Main Program --------

records = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"},
    {"id": 3, "name": "Charlie"},
    {"id": 2, "name": "Bob"}
]

print("Original list:")
print(records)

# Call the function
result = remove_duplicates(records)

print("\nList after removing duplicates:")
print(result)




OUTPUT:

Original list:
[{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 1, 'name': 'Alice'}, {'id': 3, 'name': 'Charlie'}, {'id': 2, 'name': 'Bob'}]

List after removing duplicates:
[{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]
