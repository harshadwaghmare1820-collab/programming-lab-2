# Class and Objects

# Creating a class
class Student:
    
    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

s1 = Student("Harshad", 75) # object

s1.display()
s1.result()