
# union() method returns a new set containing all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # => set(['a', 1, 'c', 'b', 3, 2])

# update() method inserts the items into set:
set1 = {"a", "b", "c"}
set2 = {1, 2}
set1.update(set2)
print(set1) # => {1, 2, 'a', 'c', 'b'}