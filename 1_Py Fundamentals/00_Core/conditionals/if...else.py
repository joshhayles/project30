
# if statement
a = 30
b = 200
if b > a:
    print("Yes!") # => Yes!

# elif (else, if) keyword
a = 200
b = 200
if b > a:
    print("Yes!")
elif a == b:
    print("a and b are equal") # => a and b are equal

# else keyword (catches anything not caught by the preceding conditions)
a = 30
b = 200
if a > b:
    print("A is greater than B")
elif a == b:
    print("A and B are equal")
else:
    print("B is greater than A") # => B is greater than A

# with only one statement to execute, you can put it on the same line
if a > b: print("A is greater than B")

# short hand if...Else (with only one statement)
a = 2
b = 4
print("A is greater") if a > b else print("B is greater than A")

# multiple if...else statements on one line
a = 30
b = 40
print("A") if a > b else print("=") if a == b else print("B")