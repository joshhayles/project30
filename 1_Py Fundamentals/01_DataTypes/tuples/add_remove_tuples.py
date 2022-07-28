
# you can add tuples together
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # => ('apple', 'banana', 'cherry', 'orange')

# removing items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("cherry")
thistuple = tuple(y)

print(thistuple) # => ('apple', 'banana')

# delete completely
thistuple = ("apple", "banana", "cherry")
del thistuple

print(thistuple) # => NameError: name 'thistuple' is not defined