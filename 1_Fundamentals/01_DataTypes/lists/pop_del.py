
# removed specified index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # => ['apple', 'cherry']

# if you don't specify the index, pop() removes the last item

# del will also delete specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]

# or use del to delete completely 
del thislist