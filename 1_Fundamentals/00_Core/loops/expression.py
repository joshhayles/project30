
# an expression is the current item in the iteration, but it is also the outcome, which can be manipulated:

# uppercase items
fruits = ["apple", "banana", "cherry"]

newlist = [x.upper() for x in fruits]

print(newlist) # => ['APPLE', 'BANANA', 'CHERRY']

# set all values in the new list to "hello"
fruits = ["apple", "banana", "cherry"]

fruitlist = ["hello" for x in fruits]

print(fruitlist) # => ['hello', 'hello', 'hello']

# the expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# return 'orange' instead of 'banana'
fruits = ["apple", "banana", "cherry"]

thelist = [x if x != "banana" else "orange" for x in fruits]

print(thelist) # => ['apple', 'orange', 'cherry']