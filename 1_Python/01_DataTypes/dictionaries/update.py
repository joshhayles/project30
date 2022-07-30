
# the update() method will update the dictionary with the items from the given argument. The argument must be a dictionary, or an iterable object with key:value pairs

# update the "year" by using update():
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2022})
print(thisdict["year"]) # => 2022

thisdict.update({"brand": "Rockin"})
print(thisdict["brand"]) # => Rockin