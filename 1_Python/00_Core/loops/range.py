
# use range() function to create an iterable
#newlist = [x for x in range(7)]
#print(newlist) # => [0, 1, 2, 3, 4, 5, 6]

# accept only numbers lower than 5
#newlist = [x for x in range(6) if x < 4]
#print(newlist) # => [0, 1, 2, 3]

# range of 6
#for x in range(6):
    #print(x) # => prints 0 - 5 vertically

# range function defaults to 0 as a starting value, however, you can specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#for x in range(2, 6):
    #print(x) # => prints 2 - 5

# you can also add a third paramter:
for x in range(2, 30, 3):
    print(x) # => prints using range between 2 and 30, incrementing by 3