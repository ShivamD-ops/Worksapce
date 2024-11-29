def greet(name):
    def display_name():
        print("Hi",name)
    
    display_name()

greet('Jhon Doe')

# Closures ------>--------
# Nested function help us access
# the outer function variables even after
# 
def greet():
    name = "Jhon"
    return lambda : "Hi " + name

msg = greet()


print(msg())


def make_mltiplier_of(n):
    def multiplier(x):
        print(f'n value is: {n}')
        print(f'x value is: {x}')
        print(f'---------------')
        return x*n
    return multiplier

times3 = make_mltiplier_of(3)
times5 = make_mltiplier_of(5)

print(times3(9))
print(times5(9))