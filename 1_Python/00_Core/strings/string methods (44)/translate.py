
# returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
# use the maketrans() method to create a mapping table

#use a dictionary with ascii codes to replace 80(P) with 83(S):
mydict = {80: 83}
txt = "Hello Sam!"
print(txt.translate(mydict)) # => Hello Pam!
