
# try block lets you test a block of code for errors

# except block lets you hanlde the error

# else block lets you execute code when there are no errors

# finally block lets you execute the code, regardless of the result of the try and except blocks

# the try block will generate an exception, because x is not defined:
# try:
#     print(x)
# except:
#     print("An exception occured") # => An exception occured

# else can be used to define a block of code that runs if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("It worked!") # => It worked!

# the finally block, if specified, will be executed regardless if the try block raises an error or not:
# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished") # => The 'try except' is finished
