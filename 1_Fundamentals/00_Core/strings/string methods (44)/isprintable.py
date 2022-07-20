
# returns true if all characters in a string are printable

txt = "are you \printable?"
print(txt.isprintable()) # => True

txt = "are you printable\n"
print(txt.isprintable()) # => False

