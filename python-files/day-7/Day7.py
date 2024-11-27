# number = int(input('Enter a number: '))
number = 90
if number > 0:
    print(f'{number} is a positive number.')
print('Astatement outside the if statement')

# n = int(input("enter a number"))
n = number
if n > 0 :
    print("Positive")
elif n == 0:
    print("Zero")
else :
    print("Negative")

match 0:
    case 1: print("here")
    case _: print("not here")

def num_to_string(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two"
    }
    return switcher.get(argument,"nothing")

match 0:
    case 1: print("here")
    case _: print("not here")