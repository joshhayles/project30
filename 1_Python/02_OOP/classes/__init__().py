
# all classes have a function called __init__(), which is always executed when the class is being initiated. You can use this function to assign values to object properties, or other operations that are necessary to do when the object is being created.

# create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Josh", 41)

print(person.name)
print(person.age)
# Josh 41