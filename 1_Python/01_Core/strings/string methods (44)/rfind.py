
# finds the LAST occurance of the specified value
# returns -1 if the value is not found
# same as rfound, except rfind returns -1 if string isn't found. rindex throws an exception

# string.rfind(value, start, end)
    # value is required
txt = "Mi casa, su casa"
print(txt.rfind("su")) # => 9

txt2 = "hello, dude!"
print(txt2.rfind("dude")) # => 7