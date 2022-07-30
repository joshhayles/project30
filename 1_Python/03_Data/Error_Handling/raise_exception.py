
# use the raise keyword to throw (raise) an exception.

# stop the program if x is lower than 0:
# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero!")

# print(x) # => Exception: Sorry, no numbers below zero!

# you can define what kind of error to raise, and the text to print to the user:
y = "hello"

if not type(y) is int:
    raise TypeError("Only integers allowed, please")

print(y)