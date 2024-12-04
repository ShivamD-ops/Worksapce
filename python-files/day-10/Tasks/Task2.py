print('''
1)
basic = lambda x,y : x + y

print(basic(2,3))
''')
basic = lambda x,y : x + y

print(basic(2,3))

print('''
2)
list1 = [1,2,3,4,5]
list2 = list(map(lambda x : x*2 , list1))
print(list2)
''')

list1 = [1,2,3,4,5]
list2 = list(map(lambda x : x*2 , list1))
print(list2)

print('''
3)
list3 = [1,2,3,4,5]
list4 = list(filter(lambda x : x%2 == 0 , list1))
print(list4)
''')

list3 = [1,2,3,4,5]
list4 = list(filter(lambda x : x%2 == 0 , list1))
print(list4)

print('''
4)
list5 = [(1,2),(4,1),(3,0),(5,1)]
list6 = sorted(list5,key = lambda x : x[1])
print(list6)
''')

list5 = [(1,2),(4,1),(3,0),(5,1)]
list6 = sorted(list5,key = lambda x : x[1])
print(list6)

'''
1) lambda is a anonymous function 
it is used for simpilar inline function use cases

2) yes we can use lambda function without sorted,map and filter
lambda can be used in squaring a number
square = lambda x : x**2
print(square(3)) -> 9

3) Lambda functions can only have one expression and the value of that expression is returned automatically.
meaning that they cannot contain multiple statements or complex control flow.

'''


