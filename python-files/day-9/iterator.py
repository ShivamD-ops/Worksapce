my_list = [10,20,30]

iterator = iter(my_list)

#get first element of the iterator

print(f'''
my_list = [10,20,30]

iterator = iter(my_list)

#get first element of the iterator

print(next(iterator))
{next(iterator)}
''')

my_list = [1,2,3,4,5]
iterator = iter(my_list)


print(f''' 
my_list = [1,2,3,4,5]
iterator = iter(my_list)
for element in iterator:
    print(element)
''')
for element in iterator:
    print(element)

#custom Iterator
print(
    '''Implementation of cutom iterator for powers of 2
class PowTwo:
    def __init__(self,maxi = 0):
        self.maxi = maxi

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.maxi:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(3)
i = iter(numbers)

for i in PowTwo(3):
    print(i)'''
)
class PowTwo:
    def __init__(self,maxi = 0):
        self.maxi = maxi

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.maxi:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(3)
i = iter(numbers)

print(numbers)

for i in PowTwo(3):
    print(i)







