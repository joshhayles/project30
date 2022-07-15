# many values to multiple variables

x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)
# => orange banana cherry

# one value to multiple variables

x = y = z = "wuzzup"
print(x)
print(y)
print(z)
# => wuzzup wuzzup wuzzup

# unpacking variables in a list and assigning them

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits 
print(x)
print(y)
print(z)