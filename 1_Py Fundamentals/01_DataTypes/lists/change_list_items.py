
thislist = ["apple", "banana", "cherry"]
thislist[1] = "Josh"
print(thislist) # => ['apple', 'Josh', 'cherry']

# change a range of item values (second index in range removed the one before it)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["Josh", "Joshua"]
print(thislist) # => ['apple', 'Josh', 'Joshua', 'orange', 'kiwi', 'mango']

# change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # => ['apple', 'blackcurrant', 'watermelon', 'cherry']

# change second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)