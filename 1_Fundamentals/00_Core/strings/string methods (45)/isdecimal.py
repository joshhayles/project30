
# returns true if all characters in a string are decimals
txt = "yes"
print(txt.isdecimal()) # => False

txt2 = "2"
print(txt2.isdecimal()) # => True

txt3 = "2.65"
print(txt3.isdecimal()) # => False