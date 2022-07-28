
# returns true if all characters in string are alphanumeric

txt = "Joshua41"
print(txt.isalnum()) # => True

txt = "JoshuabuyPRO##"
print(txt.isalnum()) # => False

txt2 = "Hello0#"
print(txt2.isalnum()) # => False