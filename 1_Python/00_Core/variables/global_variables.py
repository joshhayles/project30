
# variables created outside of a function
# x = "awesome"

# def myfunc():
#     print("Python is " + x)

# myfunc() # => Python is awesome

# if you create a variable with the same name inside a function, the variable will be local, and can only be used inside the function. The global variable will remain as it was.
x = "awesomest"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
# => Python is fantastic
# => Python is awesomest

# to create a global variable inside a function, use the global keyword
def myfunc():
    global x
    x = "fantastico"

myfunc()

print("Python is " + x)

# use global keyword if you want to change a global variable inside a function 
x = "awesomer"

def myfunc():
    global x
    x = "fantastical!"

myfunc()

print("Python is " + x)