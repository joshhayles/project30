
# print only if "free" is present
txt = "Best things in life are free"
if "free" in txt:
    print("Yes!!")

txt = "hello!!"
if "e" in txt:
    print("yep")

# check if NOT present
txt = "I love thai"
if "dud" not in txt:
    print("no")

# check if NOT and return True or False
txt = "Best things in life are free"
print("expense" not in txt) # => True