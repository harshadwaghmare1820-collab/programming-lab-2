# Experiment 2: Control Statements

# 1. Decision Making 
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# 2. For Loop
n = int(input("\nEnter number for factorial: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


# 3. While Loop 
num = int(input("\nEnter number to reverse: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed Number =", rev)


# 4. Break 
print("\nFirst multiple of 7 between 1 to 50:")
for i in range(1, 51):
    if i % 7 == 0:
        print(i)
        break


# 5. Continue 
print("\nOdd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# 6. Pass 
print("\nPass Example:")
for i in range(3):
    pass
print("Loop executed using pass")

