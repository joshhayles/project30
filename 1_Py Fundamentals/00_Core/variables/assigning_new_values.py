
# each identifier is implicitly associated with the memory address of the object to which it refers
# it can also be assigned to a special object named None
# The temperature identifier has been assigned to a new value, while original continues to refer to the previously existing value

temperature = 98
temperature = temperature + 2

print(temperature) # 100
print(type(temperature))