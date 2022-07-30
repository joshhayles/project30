
# objects can also contain methods. Methods in objects are functions that belong to the object.

# insert a function that prints a greeting, and execute it on the person object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print("Hi! My name is " + self.name)

person = Person("Josh", 41)
person.myfunction() # => Hi! My name is Josh
