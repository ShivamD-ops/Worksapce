'''
a Generator is function that returns
an iterator that produces a sequence of values
when iterated over.

Generator are useful when we want to produce a large 
sequence of values,
but we dont want to store all of then in memory at once.

syntax: 
def generator_name(arg):
    yeild something....
yeild key word is used to produce a value from
the generator.

when a generator function is called it doesnot 
execute the function body innediatly.
instead it rereturns a generator object that can
be iterated over to produce the values

'''
def my_generator(n):
    #initialize counter
    value = 0

    #loop until counter is less than n
    while value < n:
        #produce the current value of the counter
        yield value
        # increment the counter
        value += 1

for value in my_generator(3):
    # print each value produced by generator
    print(value)

print("========================")
gen = my_generator(3)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) 

# '''
# Traceback (most recent call last):
#   File "C:\Users\shivam.devaser\Desktop\git_bas
# ics\Worksapce\python-files\day-9\generator.py",
#  line 42, in <module>
#     print(next(gen))
#           ~~~~^^^^^
# StopIteration

# '''