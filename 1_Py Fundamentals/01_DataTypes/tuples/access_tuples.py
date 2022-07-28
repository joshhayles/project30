
# refer to the index to access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # => banana

# accessing negative indicies
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # => cherry

# range of indexes (does NOT include last index)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi")
print(thistuple[1:3]) # => ('banana', 'cherry')

# this example returns the items from the beginning to, but NOT including, "kiwi"
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # => ('apple', 'banana', 'cherry', 'orange')

# or from 'banana' to the end
print(thistuple[1:]) # => ('banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

# negative indexes that returns negative 4 (included) to -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # => ('orange', 'kiwi', 'melon')

# check if item exists
thistuple = ("apple", "banana", "cherry")
if "cherry" in thistuple:
    print("Yep! It's here") # => Yep! It's here