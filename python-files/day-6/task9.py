# 1
# inp = int(input("Enter a number : "))
# print(f'{10/inp}')

# 2
try:
    inp = int(input("Enter a number : "))
    print(f'{10/inp}')
except Exception as e:
    print(f'error occured in devision {e}')

print("code countinues")

# if we write except ZeroDivisionError only 
# this error will be handled
# if we write except Exception
# all type of error can be handled
