def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()
print(odd())
print(odd())
print(odd())

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)

result = add_five(6)
print(result)

def add(x,y):
    return x + y
# Pass Function as a argument
def calculate(func,x,y):
    return func(x,y)

result = calculate(add,4,6)
print(result)
# Decorators -> IMP




