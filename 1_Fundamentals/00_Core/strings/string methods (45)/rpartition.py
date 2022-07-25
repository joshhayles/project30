
# searches for LAST occurance of a specified string, and splits the string into a tuple containing three elements: before specified string, the specified string, part after the string

txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("bananas"))