
# get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# or ...
y = thisdict.get("model")
print(x) # => Mustang
print(y) # => Mustang

# keys() will return all the keys:
z = thisdict.keys()
print(z) # => dict_keys(['brand', 'model', 'year'])

# add a new item to the original dictionary:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

car["color"] = "White"
print(car) # => {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}

# values() method returns a list of all the values in a dictionary
x = car.values()
print(x) # => dict_values(['Ford', 'Mustang', 1964, 'White'])

# items() method will return each item in a dictionary, as tuples in a list.

# get a list of key:value pairs:
x = car.items()
print(x) # => dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'White')])

# update/change using items()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change