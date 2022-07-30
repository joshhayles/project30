
# returns a new string that replaces all keys in the string with the value

dict_map = {"Go": "Python", "site": "askPy"}
fmt_string = "Hello, from {site}. {site} is where you can learn {Go}."
print(fmt_string.format_map(dict_map))
# => Hello, from askPy. askPy is where you can learn Python.