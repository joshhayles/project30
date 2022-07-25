
# add "yellow" to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("yellow")
print(thisset) # => set(['cherry', 'apple', 'yellow', 'banana'])

# adding items from another set using update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # => set(['mango', 'papaya', 'apple', 'pineapple', 'cherry', 'banana'])

# the object in the update() method does not have to be a set. It can be any iterable object (tuples, lists, dictionaries)

# add elements of a list to a set:
thisset = {"apple", "banana", "strawberry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) # => set(['kiwi', 'strawberry', 'orange', 'apple', 'banana'])