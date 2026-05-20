# 1. Creating Lists
list1 = [10, 20, 30, 40]
list2 = [1, "Python", 3.5, True]

print("Original List1:", list1)
print("Mixed List2:", list2)

# 2. Accessing Elements
print("\nIndexing:")
print("First element:", list1[0])
print("Last element:", list1[-1])

# 3. Slicing
print("\nSlicing:")
print("1 to 3:", list1[1:4])
print("Reverse:", list1[::-1])

# 4. Changing Elements
list1[1] = 200
print("\nAfter Modification:", list1)

# 5. Adding Elements
list1.append(50)
list1.insert(1, 15)
list1.extend([60, 70])
print("\nAfter Adding Elements:", list1)

# 6. Removing Elements
list1.remove(15)
list1.pop()
print("\nAfter Removing Elements:", list1)

# 7. List Operations
a = [1, 2]
b = [3, 4]
print("\nConcatenation:", a + b)
print("Repetition:", a * 3)

# 8. List Functions
print("\nFunctions:")
print("Length:", len(list1))
print("Max:", max([10, 5, 20]))
print("Min:", min([10, 5, 20]))
print("Sum:", sum([10, 5, 20]))

# 9. Sorting
num_list = [5, 2, 8, 1]
num_list.sort()
print("\nSorted:", num_list)
num_list.sort(reverse=True)
print("Descending:", num_list)

# 10. Copying Lists
copy_list = list1.copy()
print("\nCopied List:", copy_list)

# 11. Looping
print("\nLooping:")
for i in list1:
    print(i, end=" ")

print("\nUsing index:")
for i in range(len(list1)):
    print(list1[i], end=" ")

# 12. Membership
print("\n\nMembership:")
print(20 in list1)
print(100 not in list1)
