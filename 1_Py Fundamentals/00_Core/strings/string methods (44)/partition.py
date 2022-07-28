
# searches for a specified string and returns a tuple where the string is parted into three parts:
    # first element contains the part before the specified string
    # second element contains specified string
    # third element contains the part after the string

txt = "I could eat bananas all day"
print(txt.partition("day")) # => ('I could eat bananas all ', 'day', '')

txt2 = "This is partition!"
print(txt2.partition("is")) # => ('Th', 'is', ' is partition!')