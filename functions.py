def greet():
    print("Hello, welcome to Python")

greet()

def add(a,b):
    print("Sum : ",a+b)
add(18,8)

def multiply(a,b):
    return a*b
result = multiply(23,5)
print(result)

def factorial(n):
    #base case
    if (n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1) #recursive call
result = factorial(5)
print("factorial of the given number is : ",result)

x = 10   #global
def show():
    y = 5   #local
    print(x,y)
show()

def outer_function(msg):
    def inner_function():
        print("messege : ",msg)
    return inner_function()

result =  outer_function("Hello Siyuu")
print(result)

def decorator_func(original_func):
    def wrapper():
        print("Before function execution")
        original_func()
        print("After function execution")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()
