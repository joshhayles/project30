
x = str("Hello")
print(x)

x = int(20)

x = float(20.5)

x1 = complex(1j)
print(x1)

x2 = list()
print(x2) # => []

x3 = list(("apple", "banana", "cherry"))
print(x3) # => ['apple', 'banana', 'cherry']

x4 = tuple(("apple", "banana", "cherry"))
print(x4) # => ('apple', 'banana', 'cherry')

x5 = range(6)
print(x5) # => [0, 1, 2, 3, 4, 5]

x6 = dict(name="Josh", age=41)
print(x6) # => {'age': 41, 'name': 'Josh'}

x7 = set(("apple", "banana", "cherry"))
print(x7) # set(['cherry', 'apple', 'banana'])

x8 = frozenset(("apple", "banana", "cherry"))
print(x8) # => frozenset(['cherry', 'apple', 'banana'])

x9 = bool(5)
print(x9) # True

x10 = bytes(5)
print(x10) # 5

x11 = bytearray(5)
print(type(x11)) # bytearray

x12 = memoryview(bytes(5))
print(type(x12)) # memoryview