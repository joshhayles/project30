
# returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
# use the maketrans() method to create a mapping table

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict)) # => Hello Pam!
