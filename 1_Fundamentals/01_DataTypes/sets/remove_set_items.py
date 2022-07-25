
# remove "banana" with remove() method:
thisset = {"banana", "apple", "cherry"}
thisset.remove("banana")
print(thisset) # => set(['cherry', 'apple'])

# remove "banana" with discard() method:
# note: this method will NOT raise an error if item does not exist
thisset = {"banana", "apple", "cherry"}
thisset.discard("banana")
print(thisset) # => set(['cherry', 'apple'])

# pop() method removes last item:
thisset = {"banana", "apple", "cherry"}
thisset.pop()
print(thisset) # => set(['banana', 'apple'])

# clear() method empties the set:
thisset = {"banana", "apple", "cherry"}
thisset.clear()
print(thisset)