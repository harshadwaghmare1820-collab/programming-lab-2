# 1) Single Inheritance

class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")


c = Child() #object 

c.show_parent()
c.show_child()

# 2) Multiple Inheritance

class Father:
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")


c = Child()     # Object 

c.show_father()
c.show_mother()
c.show_child()

# Inheritance with Constructor

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show(self):
        print("Marks:", self.marks)


s = Student("Harshad", 85)      # Object

s.display()
s.show()