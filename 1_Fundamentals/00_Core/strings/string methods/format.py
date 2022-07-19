# https://www.w3schools.com/python/ref_string_format.asp

# formats specified vales into a string
txt = "My name is {first_name}, I'm {age}".format(first_name = "Josh", age = 41)
print(txt) # => My name is Josh, I'm 41

# you can also use inicies 
txt2 = "My name is {0}, I'm {1}".format("Joshua", 42)
print(txt2) # => "My name is Joshua, I'm 42"

# inside the placeholders you can add a formatting type to format the result (see URL above for formatting list)

# :< left aligns result
txt2 = "My name is {0}, I'm {1:<}".format("Joshua", 42)
print(txt2)

# fixed point, two decimal format
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 4900))