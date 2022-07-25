
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) # => {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# or use dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict) # => {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}