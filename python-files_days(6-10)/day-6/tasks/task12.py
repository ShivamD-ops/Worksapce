list1 = [1,2,3,4,5]
print(f'initial list{list1}')
list1.append(6)
print(f'6 appended list{list1}')
list1.pop(0)
print(f'poped from front list {list1}')
list1[2] = 2 #zero based index
print(f'updated 2nd index list {list1}')

# print(list1[9])
# If we try to access index that doesnot exist 
# in the given list then 
# IndexError: list index out of range error occurs