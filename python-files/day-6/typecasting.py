num1 = 3
num2 = 2.2

#implicit type conversion 
res = num1 + num2
print(f"val-> {res} Type-> {type(res)}")

#string to int implicit conv can not happen

#explicit
num1 = 123
num2 = "456"
res = num1 + int(num2)
print(f"val-> {res} Type-> {type(res)}")

# Output formatting
x = 1
y = 2
print('the value of x is {} and y is {}'.format(x,y))
