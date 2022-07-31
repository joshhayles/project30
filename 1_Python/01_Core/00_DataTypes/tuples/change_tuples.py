
# once tuples are created, they're immutable, but there is a workaround. You can convert the tuple to a list, change the list, then convert the list back into a tuple

# step1: convert tuple into a list
x = ("apple", "banana", "cherry")
y = list(x) # y = a list that takes in 'x' as an argument

# step2: create new value and target the index you want to update/change
y[1] = "kiwi" # => targets "banana" | Note: you can also use y.append("kiwi") to add it to the end of the list

# step3: convert it back to a tuple
x = tuple(y)

print(x) # => ('apple', 'kiwi', 'cherry')

# done without comments
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)