
import json

# json.dumps() has parameters to make it easier to format and read.

# indent, separators, and sort_keys parameters are used to format the JSON data and make it more legible:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json.dumps(x, indent=4, separators=(". ", " = "))

print(x) # => {'name': 'John', 'age': 30, 'married': True, 'divorced': False, 'children': ('Ann', 'Billy'), 'pets': None, 'cars': [{'model': 'BMW 230', 'mpg': 27.5}, {'model': 'Ford Edge', 'mpg': 24.1}]}