
import re
# python has a built-in module to help with regular expressions.

# search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a match.")
else:
    print("No match") # => Yes! We have a match.