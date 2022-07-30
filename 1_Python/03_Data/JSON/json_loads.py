
# python has a built-in package called json to work with json data:
import json

# if you have a json string, you can parse it by using the json.loads() method. The result will be a dictionary.

# convert from json to python:
x = '{"name":"Josh", "age":41, "city":"Springs"}'

# parse x:
y = json.loads(x)

print(y) # => {'name': 'Josh', 'age': 41, 'city': 'Springs'}
print(y["age"]) # => 41