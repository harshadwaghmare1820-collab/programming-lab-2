# 1. Creating Dictionary
dict1 = {"name": "Harshad", "age": 20, "city": "Pune"}
dict2 = dict(a=10, b=20, c=30)

print("Original Dictionary:", dict1)
print("Second Dictionary:", dict2)

# 2. Accessing Elements
print("\nAccessing Elements:")
print("Name:", dict1["name"])
print("Age:", dict1.get("age"))

# 3. Adding Elements
dict1["course"] = "B.Tech"
print("\nAfter Adding:", dict1)

# 4. Updating Elements
dict1["age"] = 21
print("\nAfter Updating Age:", dict1)

# 5. Removing Elements
dict1.pop("city")
print("\nAfter pop():", dict1)

dict1.popitem()   #removes last inserted item
print("After popitem():", dict1)

# 6. Dictionary Operations
dictA = {"x": 1, "y": 2}
dictB = {"z": 3}

merged = {**dictA, **dictB}
print("\nMerged Dictionary:", merged)

# 7. Dictionary Functions
print("\nFunctions:")
print("Length:", len(dict1))
print("Max key:", max(dict2))
print("Min key:", min(dict2))

# 8. Keys, Values, Items
print("\nKeys:", dict2.keys())
print("Values:", dict2.values())
print("Items:", dict2.items())

# 9. Looping Through Dictionary
print("\nLooping:")
for key in dict2:
    print(key, dict2[key])

print("\nUsing items():")
for k, v in dict2.items():
    print(k, v)

# 10. Copying Dictionary
copy_dict = dict1.copy()
print("\nCopied Dictionary:", copy_dict)

# 11. Membership Operators
print("\nMembership:")
print("name" in dict1)
print("salary" not in dict1)

