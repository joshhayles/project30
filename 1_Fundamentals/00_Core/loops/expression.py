
# an expression is the current item in the iteration, but it is also the outcome, which can be manipulated:

# uppercase items
fruits = ["apple", "banana", "cherry"]
newlist = [x.upper() for x in fruits]
print(newlist) # => ['APPLE', 'BANANA', 'CHERRY']