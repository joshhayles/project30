
# fromkeys() returns a dictionary with the specified keys and the specified value | dict.fromkeys(keys, value)

# this creates a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict) # => {'key1': 0, 'key2': 0, 'key3': 0}