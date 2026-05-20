# Exception Handling

# ZeroDivisionError : 

print("Exception Handling Example")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input (only numbers allowed)")

finally:
    print("Program executed successfully")


# List Index Error : 

try:
    lst = [10, 20, 30]
    print("Accessing element:", lst[5])

except IndexError:
    print("Error: Index out of range")