
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy()

# copy()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # => ['apple', 'banana', 'cherry']