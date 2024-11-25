# Step - 1
a = 1
b = 2.2
c = "3.3"
d = False

# Step - 2
res1 = a+b
res2 = a-b
res3 = a*b
res4 = a**2
print(f"{a} + {b} = {res1},{a} - {b} = {res2}, {a} * {b} = {res3},{a}^{b} = {res4}")


# print(a + "1") #error
#TypeError: unsupported operand type(s) for +: 'int' a
# nd 'str
print(a + int("1"))
# python checks type at runtime
# i.e. datatype is handled at runtime not compiletime
# python automaticaly handles type conversion in operations
# if error occurs it raises type error


