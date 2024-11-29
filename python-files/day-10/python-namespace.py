#python namespace and scope
'''
namespace -> collection of names [uniquw name for each and every obj in python]

Builtin namespace -> created when python interpretor starts
and exists as long as interpretor runs.
ex-> print(), id() etc...


Global namespace -> Each module creates its global namespace

local namespace -> created when function is called.

'''

global_var = 10

def outer_function():
    outer_var = 20

    def inner_function():
        inner_var = 30

        print(inner_var)
    
    print(outer_var)

    inner_function()

print(global_var)

outer_function()

## Global Key word

def my_func():
    local_var = 20
    # global global_var
    global_var = 30

print(global_var)
my_func()
print(global_var)

