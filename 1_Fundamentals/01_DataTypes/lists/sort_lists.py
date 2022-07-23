
# sorts alphanumerically, ascending by default (also works sorting numbers):
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist) # => ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# sort descending using reverse = True (also works on numbers)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist) # => ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50) # abs() function returns the absolute value of the given number

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist) # => [50, 65, 23, 82, 100]

# sort() is case sensitive, resulting in capital letters being sorted before lower case:
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist) # => ['Kiwi', 'Orange', 'banana', 'cherry']

# using str.lower will make it case-insensitive:
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist) # => ['banana', 'cherry', 'Kiwi', 'Orange']

# reverse the current sorting order of the elements (reads it backwards)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.reverse()

print(thislist) # => ['banana', 'pineapple', 'kiwi', 'mango', 'orange']