
# use range() function to create an iterable
newlist = [x for x in range(7)]
print(newlist) # => [0, 1, 2, 3, 4, 5, 6]

# accept only numbers lower than 5
newlist = [x for x in range(6) if x < 4]
print(newlist) # => [0, 1, 2, 3]