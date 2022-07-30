
thislist = ["apple", "banana", "cherry"]
print(thislist[2]) # => cherry

# negative indexing (start from the end)
thislist = ["apple", "banana", "cherry"]
print(thislist[-2]) # => banana

# specify a range (last index is excluded)
thislist = ["apple", "banana", "cherry"]
print(thislist[0:2]) # => ['apple', 'banana'] 
print(thislist[:2]) # => ['apple', 'banana'] 
print(thislist[1:]) # => ['banana', 'cherry']

# range of negatives that returns the items from "orange"(-4) to, but NOT including "mango"(-1)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # => ['orange', 'kiwi', 'melon']

# check if something exists
thislist = ["apple", "banana", "cherry"]
if "josh" in thislist:
    print("Yep. It's there!")
else:
    print("Nope. Can't find it.")