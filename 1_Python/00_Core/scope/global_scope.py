
# variable outside the function is global and can be used by anyone:
x = 305

def myfunc():
    print(x)

myfunc()

print(x) # => 305

# function will print the local x, then the global x:
x = 500

def myfunc():
    x = 200
    print(x)

myfunc()

print(x) # => 200 500

# use global keyword to change the value of a global variable
x = 800

def myfunc():
    global x
    x = 33

myfunc()

print(x) # => 33