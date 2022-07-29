
# to create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    pass