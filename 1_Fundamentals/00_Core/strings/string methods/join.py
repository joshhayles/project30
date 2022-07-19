
# joins elements of an iterable to the end of the string

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

print(mySeparator.join(myDict)) # => nameTESTcountry

# you can also join all items in a tuple into a string, using a hash character as separator 

myTuple = ("John", "Peter", "Vicky")

print("#".join(myTuple)) # => John#Peter#Vicky