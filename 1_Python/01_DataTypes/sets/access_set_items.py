
# you can not access items in a set by index or key. But, you can loop through a set using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# loop through a set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x) # => cherry apple banana

# check if "banana" is present:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # => True

# print custom message:
thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
    print("Yep. It's here")