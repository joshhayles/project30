
# the super() function will make the child class inherit all the methods and properties from its parent:

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

# adding properties
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019 # 2019 becomes a variable that can be passed to the Student class when creating student objects. Add another parameter in the __init_() function: