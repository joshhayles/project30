# https://www.w3schools.com/python/ref_string_maketrans.asp

# returns a mapping table that can be used with the translate() method to replace specified characters

# string.maketrans(x, y, z)

txt = "Hi, Sam!"
x = "mSa"
y = "eJo"
table = txt.maketrans(x, y) 
print(table) # => {109: 101, 83: 74, 97: 111}

print(txt.translate(table)) # => Hi, Joe!

