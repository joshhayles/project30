
# and keyword returns true if both statements are true
a = 200
b = 30
c = 500
if a > b and c > a:
    print("Both conditions are true")

# or keyword returns true if one of the statements is true
a = 200
b = 30
c = 500
if a > b or a > c:
    print("At least one condition is true")

# reverse the result, returns false if the result is true
# not(x < 5 and x < 10)
x = 4
print(not(x < 5 and x < 10)) # => False