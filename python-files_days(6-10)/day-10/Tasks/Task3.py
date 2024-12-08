print('''
class Range:
    def __init__(self,start = 0, end = 0):
        self.start = start
        self.end = end

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n + self.start <= self.end:
            result = self.n + self.start
            self.n += 1
            return result
        else:
            raise StopIteration

for i in Range(2,10):
    print(i)

''')

class Range:
    def __init__(self,start = 0, end = 0):
        self.start = start
        self.end = end

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n + self.start <= self.end:
            result = self.n + self.start
            self.n += 1
            return result
        else:
            raise StopIteration

for i in Range(2,10):
    print(i)

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

print("-----------------------------")
test_list = [1,2,3,4,5,6]
iterator_1 = iter(test_list)
while 1:
    try:
        print(next(iterator_1))
    except StopIteration:
        print(f"Stop iteration trigered")
        break

'''
1) iterator is an pointer to a address block
list is an data structure to store values at a address block
iterator can point to that block

2) when a iterator reaches end of sequence and no value is present there the StopIteration Exception is triggered
eg-> as in while loop example.

3) __iter__() is used to initialize the iterator
when created

'''
    
