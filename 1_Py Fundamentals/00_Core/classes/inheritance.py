
# inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called the base class.
# Child class is the class that inherits from another class, also called derived class.

# create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Josh", "Hayles")
x.printname() # => Josh Hayles
