
# all objects have a iter() method which is used to get an iterator. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

# return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) # => apple
print(next(myit)) # => banana
print(next(myit)) # => cherry

# strings are also iterable:
mystr = "banana"
myit = iter(mystr)

print(next(myit)) # => b
print(next(myit)) # => a