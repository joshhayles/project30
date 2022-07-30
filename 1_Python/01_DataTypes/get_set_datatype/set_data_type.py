# data type is set when you assign a value to a variable

x = "Hello, world!" # str
x = 20 # int
x = 20.5 # float
x1 = 1j # complex [of numeric type]
print(type(x1))
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x2 = {"name" : "John", "age" : 36} # dict
x3 = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" #bytes
x4 = bytearray(5) #bytearray
print(type(x4))
x5 = memoryview(bytes(5)) # memoryview
print(type(x5))
x6 = None #NoneType
print(type(x6))