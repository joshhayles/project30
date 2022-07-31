
# variable inside a function belongs to the local scope of that function, and can only be used inside that function

# variable inside a function:
def myfunc():
    x = 300
    print(x)

myfunc() # => 300

# it can also be accessed from a function within the function:
def myfun2():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfun2() # => 300