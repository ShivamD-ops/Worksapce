number = 1 #int
print(number)
print(type(number))

name = "Shivam" #string
print(name)
print(type(name))

deci = 7.90 #floor
print(deci)
print(type(deci))

boolean = True #bool
print(boolean)
print(type(boolean))

char = 'A' #string
print("char")
print(type(char))

a = [1,2,3] #list
print(a)
print(type(a))

a1 = (1,2,3) #tupple
print(a1)
print(type(a1))

b = {
    "name":name,
    "num": number,
    "deci":deci,
    "boolean":boolean,
    "list":a
}
print(b) #dict
print(type(b))
#assigning multiple vaues to multiple variables
x,y,z = "x",26,27.01
print(x)
print(y)
print(z)

msg1 = msg2 = "Welcome to Web App Dev"
print(msg1)
print(msg2)

num1 = 20
num2 = 21
sum = num1 + num2
sub  = num1 - num2
mul = num1 * num2
devide = num1 / num2
mod = num1 % 7

print("Sum of 2 numbers : ", sum)
print("Subtraction of 2 numbers : ", sub)
print("Multiplication of 2 numbers : ", mul)
print("Devision of 2 numbers : ", devide)
print("Mod of num1 with 7 : ", mod)
def addition(num1,num2):
    return num1 + num2
print("Sum of 2 numbers : ",addition(20,21))

