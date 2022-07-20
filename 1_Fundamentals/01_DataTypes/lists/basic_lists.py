
# used to store collections of data

thislist = ["apple", "banana", "cherry"]
print(thislist) # => ['apple', 'banana', 'cherry']

# list items are ordered (in the way the position they're written) changeable (can add or remove items), and allow duplicate values

print(len(thislist)) # => 3

# they can be of any data type, and have a mixture
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# lists are defined as objects with the data type 'list'
print(type(list4)) # => <class 'list'>