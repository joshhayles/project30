
# list comprehension offers a shorter syntax when creating a new list based on the values of an existing list

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) # => ['apple', 'banana', 'mango']

# with list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # => ['apple', 'banana', 'mango']

# a condition that's NOT true:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# the condition can also be omitted to print the whole list:
newlist2 = [x for x in fruits]
print(newlist2) # => ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# syntax:
# newlist = [expression for item in iterable if condition == True]
# the return value is a new list, leaving the old list unchanged

