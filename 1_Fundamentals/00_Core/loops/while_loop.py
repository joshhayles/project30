
# loop through list items
# use len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes, increasing the index by 1 after each iteration

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1 # => apple banana cherry

# using a tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1 # => apple banana cherry