
# loop through list items
# use len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes, increasing the index by 1 after each iteration

# using a list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1  # => apple banana cherry

# using a tuple
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1  # => apple banana cherry

# print i as long as i is less than 6
i = 1
while i < 10:
    print(i)
    i += 1 # => prints 1 - 9

# use the break statement to stop the loop, even if the while condition is true
i = 5
while i < 20:
    print(i)
    if i == 5:
        break # => 5
    i += 1

i = 10
while i < 20:
    print(i)
    if i == 30:
        break
    i += 1 # => prints 10 - 19
