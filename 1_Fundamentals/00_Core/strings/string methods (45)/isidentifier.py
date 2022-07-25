
# returns true if string is a valid dentifier. A string is considered a valid identifier if it only contains alphanumeric letters, 0-9 numbers, or _ underscores. It can not start with a number, or contain any spaces

txt = "demo"
print(txt.isidentifier()) # => True

txt = "2demo"
print(txt.isidentifier()) # => False

txt = " demo"
print(txt.isidentifier()) # => False


