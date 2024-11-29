try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Your age is {age}.")

while 1:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else:
        print(f"Your age is {age}.")
        break

'''
1)every input is of type string int() type casts to integer
2)when a input can not be typecasted to integer the ValueError occurs
3)we can have a while loop until exception is comming

while 1:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else:
        print(f"Your age is {age}.")
        break
'''