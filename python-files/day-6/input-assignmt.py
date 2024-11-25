num = input('Enter a number :')
print(f"You have entered: {num} and its data-type is : {type(num)}")
#default input will be str
#to make input int or any other data-type use Type casting-> int(input())
num = int(input('Enter a number :'))
print(f"You have entered: {num} and its data-type is : {type(num)}")

a = 10
b = 5

a += b
print(f"{a}")
print(f"a > b {a > b}, a != b {a!=b}, a < b {a<b}, a >= b {a>=b}")
