# 1.Creating Tuples
tuple1 = (10, 20, 30, 40)
tuple2 = (1, "Python", 3.5, True)

print("Original Tuple1:", tuple1)
print("Mixed Tuple2:", tuple2)

# 2. Accessing Elements 
print("\nIndexing:")
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])

# 3. Slicing
print("\nSlicing:")
print("1 to 3:", tuple1[1:4])
print("Reverse:", tuple1[::-1])

# 4. Tuple Immutability 
print("\nTuple is immutable (cannot change values directly)")

# 5. Adding Elements 
tuple1 = tuple1 + (50,)
print("\nAfter Adding Element:", tuple1)

# 6. Removing Elements 
temp_list = list(tuple1)
temp_list.remove(20)
tuple1 = tuple(temp_list)
print("\nAfter Removing Element:", tuple1)

# 7. Tuple Operations
a = (1, 2)
b = (3, 4)
print("\nConcatenation:", a + b)
print("Repetition:", a * 3)

# 8. Tuple Functions
print("\nFunctions:")
print("Length:", len(tuple1))
print("Max:", max((10, 5, 20)))
print("Min:", min((10, 5, 20)))
print("Sum:", sum((10, 5, 20)))

# 9. Sorting
num_tuple = (5, 2, 8, 1)
sorted_list = sorted(num_tuple)
print("\nSorted Tuple:", sorted_list)

# 10. Copying Tuple
copy_tuple = tuple1[:]   # slicing method
print("\nCopied Tuple:", copy_tuple)

# 11. Looping Through Tuple
print("\nLooping:")
for i in tuple1:
    print(i, end=" ")

print("\nUsing index:")
for i in range(len(tuple1)):
    print(tuple1[i], end=" ")

# 12. Membership Operators
print("\n\nMembership:")
print(20 in tuple1)
print(100 not in tuple1)
