print(
    '''
---------------------------------------------
1)
def count_up_to_n(n):
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
    '''
)
def count_up_to_n(n):
    #initialize counter
    value = 0

    #loop until counter is less than n
    while value < n:
        #produce the current value of the counter
        yield value
        # increment the counter
        value += 1

for value in count_up_to_n(10):
    # print each value produced by generator
    print(value)

print(
    '''
---------------------------------------------
2)
def fibo(N):
    #initialize counter
    n = 1
    n_1 = 0
    curr = 1
    cnt = 0
    yield n

    #loop until counter is less than n
    while cnt <= N:
        #produce the current value of the counter
        curr = n + n_1
        n_1 = n
        n = curr
        cnt += 1
        yield curr

for value in fibo(9):
    # print each value produced by generator
    print(value)
    '''
)

def fibo(N):
    #initialize counter
    n = 1
    n_1 = 0
    curr = 1
    cnt = 0
    yield n

    #loop until counter is less than n
    while cnt <= N:
        #produce the current value of the counter
        curr = n + n_1
        n_1 = n
        n = curr
        cnt += 1
        yield curr

for value in fibo(9):
    # print each value produced by generator
    print(value)
print(
    '''
---------------------------------------------
3)
def square(N = 10):
    #initialize counter
    cnt = 1

    while cnt <= N:
        #produce the current value of the counter
        
        yield cnt**2
        cnt += 1

for value in square():
    # print each value produced by generator
    print(value)
    '''
)

def square(N = 10):
    #initialize counter
    cnt = 1

    while cnt <= N:
        #produce the current value of the counter
        
        yield cnt**2
        cnt += 1

for value in square():
    # print each value produced by generator
    print(value)

print(
    '''
---------------------------------------------
4)
def square(N = 3):
    #initialize counter
    cnt = 1

    while cnt <= N:
        #produce the current value of the counter
        
        yield cnt**2
        cnt += 1

print("========================")
try:
    gen = square()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("StopIteration Triggered")
    '''
)

def square(N = 3):
    #initialize counter
    cnt = 1

    while cnt <= N:
        #produce the current value of the counter
        
        yield cnt**2
        cnt += 1

print("========================")
try:
    gen = square()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("StopIteration Triggered")


'''
1) yeild does not terminates funtion return terminates it

2) generators produce one value at time and can be used to get large
quatity of data
while lists just store whole data at once

3) next() points to next yeild statement
it is used as->
gen = my_generator(3)
print(next(gen))
print(next(gen))
print(next(gen))
'''
