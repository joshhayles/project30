
# Almost everything in Python is an object. A class is like an object constructor, or a "blueprint" for creating objects.

# use the class keyword
class MyClass:
    x = 5

print(MyClass) # => <class '__main__.MyClass'>

# now we can use the class named MyClass to create objects.

# create an object named p1, and print the value of x:
MyClass()
print(MyClass.x) # => 5