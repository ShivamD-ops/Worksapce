# 1a list comprehension to generate a list of squares for
# numbers 1 through 10.

squared_numbers = [i**2 for i in range(1,11)]

print(f'list comprehension to generate a list of squares for numbers 1 through 10. {squared_numbers}')

squared_numbers_even = [i**2 for i in range(1,11) if i%2 == 0]

print(f'list comprehension to generate a list of squares for even numbers 1 through 10. {squared_numbers_even}')

squared_numbers_tupple = [(i,i**2) for i in range(1,11)]

print(f'list comprehension to generate a list of squares for numbers 1 through 10. {squared_numbers_tupple}')

list1 = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list = [i for i1 in list1 for i in i1]

print(f'list comprehension to flatten a  2D list {list1} to {flatten_list}')


'''
1) List comprehession over traditional for loops helps
in compact code , faster execution, less-error-prone

2) we can add contion like if condition
like we did for even numbers

3) We can make list of cubes by simply using i**3 instead of i**2


'''



