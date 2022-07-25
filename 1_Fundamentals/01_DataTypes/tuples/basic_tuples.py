
# tuples are a data type used to store multiple items in a single variable

# tuples items are ordered, unchangeable, allow duplicate values, and written in parenthesis:

# create a tuple
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

# tuple items are indexed
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1]) # => banana

# use the len function to determine how many items a tuple has
thistuple = ('apple', 'banana', 'cherry')
print(len(thistuple)) # => 3

# to have only one item, you must have a comma after the item
thistuple = ("apple",)
print(type(thistuple)) # => <type 'tuple'>

# use the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))