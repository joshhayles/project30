
# returns true if all characters in a string are printable. Printable characters are: Digits, Uppercase Letters, Lowercase Letters, Punctuation or special Characters, and Spaces

txt = "are you \printable?"
print(txt.isprintable()) # => True

txt = "are you printable\n"
print(txt.isprintable()) # => False

txt = ""
print(txt.isprintable()) # => True

