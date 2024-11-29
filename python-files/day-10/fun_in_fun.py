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
