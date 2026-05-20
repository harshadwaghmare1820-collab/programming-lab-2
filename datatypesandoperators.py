# Experiment 1: Data Types and Operators

# Data Types
a = 10              # int
b = 5.5             # float
c = "Hello"         # string
d = True            # boolean
e = [1, 2, 3]       # list
f = (4, 5, 6)       # tuple
g = {"name": "Harshad", "age": 20}  # dictionary

print("Data Types:")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# Arithmetic Operators
x = 10
y = 3

print("\nArithmetic Operations:")
print("Add:", x + y)
print("Sub:", x - y)
print("Mul:", x * y)
print("Div:", x / y)
print("Mod:", x % y)
print("Power:", x ** y)

# Relational Operators
print("\nRelational Operations:")
print(x > y)
print(x == y)
print(x != y)

# Logical Operators
print("\nLogical Operations:")
print(x > 5 and y < 5)
print(x > 5 or y > 5)
print(not(x > 5))

# Assignment Operators
z = 5
z += 2
print("\nAssignment Operation:", z)