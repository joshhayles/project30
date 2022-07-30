
# if you have a python object, you can convert it into a JSON string using json.dumps():
import json

x = {
    "name": "Josh",
    "age": 41,
    "city": "Springs"
}

# convert into JSON
y = json.dumps(x)

print(y) # => {"name": "Josh", "age": 41, "city": "Springs"}

# when you convert from python to JSON, python objects are converted into the JSON Javascript equivalent:
# dictionary becomes an object
# list becomes an array
# tuple becomes an array
# etc