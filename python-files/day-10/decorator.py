def make_pretty(func): # some pre requisites
    def inner():
        print("i Got Decorated")
        func()
    return inner


def make_pretty2(func): # some pre requisites
    def inner():
        print("i Got Decorated again")
        func()
    return inner


print(
    '''
def ordinary():
    print("I am ordinary")


decorated_func = make_pretty(ordinary)
decorated_func()
->
    '''
)


def ordinary():
    print("I am ordinary")


decorated_func = make_pretty(ordinary)
decorated_func()
# Decorator -> its a function taking function and
# returns it by adding some functionality

# Eg->
# DP opperation -> CRUD
# prerequisite to have DB object
# Helps in adding extra functionality
print(
    '''
@make_pretty
def ordinary2():
    print("I am Ordinary 2")

ordinary2() 
->
    '''
)
@make_pretty
def ordinary2():
    print("I am Ordinary 2")

ordinary2()

print(
    '''
@make_pretty
@make_pretty2
def ordinary3():
    print("I am Ordinary 3")

ordinary3()
->
    '''
)

@make_pretty
@make_pretty2
def ordinary3():
    print("I am Ordinary 3")

ordinary3()



