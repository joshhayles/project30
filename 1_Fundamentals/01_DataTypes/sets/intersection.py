
# intersection_update() method will keep only the items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.intersection_update(x)
print(y) # => {'apple'}

# intersection() will return a NEW set that only contains the items that are present in both sets

# return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) # => {'apple'}