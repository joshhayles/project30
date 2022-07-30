
# with the break statement we can stop the loop before it has looped through all the items

# exit the loop when x is "banana":
# fruits = ["apple", "banana", "orange"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
# => apple banana (stops after looping through banana)

# fruits2 = ["apple", "banana", "orange"]
# for x in fruits2:
#     print(x)
#     if x == "apple":
#         break 
# => apple

# exit the loop when x is "banana", but this time the break comes before the print:
fruits3 = ["apple", "banana", "orange"]
for x in fruits3:
    if x == "banana":
        break
    print(x) 
# => apple

# break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("All done!") # => prints 0 - 2