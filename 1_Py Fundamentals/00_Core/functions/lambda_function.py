
# a lambda function is a small anonymous function. It can take any number of arguments, but only one expression:

# syntax: lambda arguments : expression

# add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5)) # => 15

# multiply argument a with argument b and return result:
x = lambda a, b : a * b
print(x(5, 6)) # => 30

# summarize arguments a, b, and c and return result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # => 13

# using lambda functions is great when you use them as an anonymous function inside another function. If you have a function definition that takes one argument (n) and that argument will be multipled with an unknown number (a):
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11)) # => 22