#Error-> caused by worng inputs and syntax
# it leads to program termination directly

# Exception are raised when a program is sy
# Syntactically correct, but the code results in an error

# ex :
try:
    # devidebyzero error
    number = 50
    res = 50 / 0
    print(res)
except:
    print("Exception Handled at line 14")

print("Code countinues till line 16")

# type-error
try:
    print('begin')
    x = 5
    y = "hello"
    z = x + y
    print(z)
    print('end')
except:
    print("Exception Handled at line 27")

print("Code countinues till line 29")


try:
    pass
except Exception as e:
    print(e)

def fun(a):
    if a < 4:
        b = a/(a-3)
    print("Value of b = ", b)

try:
    # fun(3)
    fun(5)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)

print("code countinues")