
# easiest way is to use the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print(list1 + list2) # => ['a', 'b', 'c', 1, 2, 3]

# using append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1) # => ['a', 'b', 'c', 1, 2, 3]

# extend() method will add list2 to the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) # => ['a', 'b', 'c', 1, 2, 3]