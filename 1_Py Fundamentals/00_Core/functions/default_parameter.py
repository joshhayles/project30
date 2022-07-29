
# if the function is called without an argument, it uses the default value:
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden") # => I am from Sweden
my_function() # => I am from Norway