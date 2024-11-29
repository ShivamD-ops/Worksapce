greet = lambda : print('welcome to lambda expressions')

greet()

greet_user = lambda name: print('Welcome', name)
greet_user('SAM')
def double_fun(x):
    return x*2
my_list = [1,2,3,4,5,6,11,3,12]
new_list = list(map(double_fun, my_list))
new_list1 = list(map(lambda x : x*2, new_list))
print(f'''
def double_fun(x):
    return x*2
my_list = [1,2,3,4,5,6,11,3,12]
new_list = list(map(double_fun, my_list))
new_list1 = list(map(lambda x : x*2, new_list))

doubled by normal function ->{new_list} \n doubled by lambda -> {new_list1}''')

even_numbers = list(filter(lambda x: (x%2 == 0), my_list))

print(f''' 
my_list = [1,2,3,4,5,6,11,3,12]
even numbers = list(filter(lambda x: (x%2 == 0), my_list))
->
{even_numbers}
''')


