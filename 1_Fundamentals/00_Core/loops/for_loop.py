
# print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x) # => apple banana cherry (listed vertically)

# iterate through items in a tuple and print the values
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x) # => apple banana cherry

# for loop in a set:
thisset2 = {"apple", "banana", "cherry"}
for x in thisset2:
    print(x)

# for loop in dictionary that prints key names:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x) # => brand model year

# or use keys()
for x in thisdict.keys():
    print(x)

# print all values
for x in thisdict:
    print(thisdict[x]) # => Ford Mustang 1964

# or use values()
for x in thisdict.values():
    print(x)

# loop through both keys and values using the items() method:
for x, y in thisdict.items():
    print(x, y)