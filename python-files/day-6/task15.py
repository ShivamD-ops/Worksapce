set1 = {i for i in range(1,20) if i%2 == 0}
set2 = {i for i in range(1,20) if i%2 != 0}
print(f'set1 of even number-> {set1}')
print(f'set2 of odd numbers-> {set2}')
#Union
print(f'union of {set1} and {set2} = {set1 | set2}')
#intersection
print(f'intersection of {set1} and {set2} = {set1 & set2}')

set3 = set()

if not set3:
    print(f"set {set3} is empty")
else:
    print(f'set {set3} is not empty')
set3.add(1)
set3.add(2)
set3.add(2)
print(set3)
# Addin multiple duplicates doen not do anything
# Set contain unique values only
