
# use the continue statement to stop current iteration, and continue with the next:

# example 1
i = 0
while i < 6:
    i += 1 # increment i by 1
    if i == 3:
        continue
    print(i) # => prints 1 - 6

# example 2
i = 3
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i) # => prints 4 - 6