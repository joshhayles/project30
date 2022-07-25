
# pop() removes the item with specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) # => {'brand': 'Ford', 'year': 1964}

# del can also be used:
del thisdict["year"]
print(thisdict) # => {'brand': 'Ford'}

# popitem() method removes the last inserted item:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # => {'brand': 'Ford', 'model': 'Mustang'}

# clear() empties dictionary
thisdict.clear()