
# intersection_update() method will keep only the items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.intersection_update(x)
print(y) # => set(['apple'])