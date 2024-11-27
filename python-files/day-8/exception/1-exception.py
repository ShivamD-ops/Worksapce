try:
    k = 50 / 0
    print(k)
except ZeroDivisionError:
    print('can not devide by zero')
finally:
    print("This is always executed")

# Raise Exception allows programmer to force a specific
# Exception to occur

try:
    raise NameError("Hi")
except Exception:
    print("an exception")
    # raise