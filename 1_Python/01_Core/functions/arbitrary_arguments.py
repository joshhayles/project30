
# if you don't know how many arguments will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
    print("Youngest kiddo is " + kids[0])

my_function("Emma", "Luke", "Paige", "Abe") # => Youngest kiddo is Emma

# Arbitrary keyword arguments (**kwargs) can be used if the number of keyword arguments is unknown:
def my_function(**kid):
    print("Last name is " + kid["lname"])

my_function(fname = "Josh", lname = "Hayles") # => Last name is Hayles


# you can also send arguments using key = value syntax
def my_function(child3, child2, child1):
    print("Youngest kiddo is " + child3)

my_function(child1 = "Emma", child2 = "Luke", child3 = "Abe") # => Youngest kiddo is Abe