
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 
# is returns true if both variables are the same object
# x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # => True (z is the same as x)
print(x == y)

# is not
# returns true if both variables are not the same object
# x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) # => False (z is the same object as x)
print(x is not y) # => True (x is not the same object as y, even if they have the same content)