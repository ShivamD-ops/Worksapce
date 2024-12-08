# ----------------------------------
# List ---------------------------------------------------------------------------
# --------------------------------------------------
print("List-------------------")
elemnets = [10,20,30]
print(elemnets)
#list: placing elemnets inside a square brackets

person = ['Jhon',45,'PythonFSD']
#ordered mutable and duplicate
print(person,person[0])#can access perticular element

print(person[-1]) # last ement, negative indexing

vowels = "a e i o u"
vowels = vowels.split(' ')
print(vowels)
print(vowels[1:2])
print(vowels[2:])
print(vowels[:])

fruits = ['apple','banana','orange']
fruits.append('cherry')
print(fruits)

# ---------------------------------
#tupples-------------------------------------------------------------------
# ---------------------------------
print("Tupple-------------------")
nums = (10,20,20,30)
print(nums)
#ordered, Immutable allows duplicate
lang = ('Python','Swift', 'C++')
print(lang[0])
print(lang[2])
print(len(lang))

for l in lang:
    print(l)
print("Python" in lang)
print("C++" in lang)

# ---------------------------------
#Set-----------------------------
#--------------------------------------------

#set--------------------
# ----------------------
print("Set-------------------")
student_id = {1000,101,102,103,104,105}
print(f'{student_id}')
student_id.add(106)
print(f'added 106 {student_id}')
student_id.discard(106)
print(f'After removel of 106 {student_id}')

print("Loop")
# to reverse sort -> descending order->
student_id = sorted(student_id)
sorted_set = student_id[::-1]
for student in student_id:
    print(f'student id: {student}')
# sorted_set = student_id[::-1]

# Intersection and Union and symmetric difference
A = {1,2,3}
B = {2,3,4}
print(f'intersection using & {A&B}')
print(f'intersection using intersection(): {A.intersection(B)}')

print(f'union using | {A | B}')
print(f'union using union() {A.union(B)}')

print(f'symmetric difference using ^ {A ^ B}')
print(f'symmetric difference using symmetric_difference {A.symmetric_difference(B)}')

print(f'Difference using - {A-B}')
print(f'Difference using difference() {A.difference(B)}')

if A == B:
    print('Set A and B are Equal')
else :
    print("Both are not equal")
print(f'Dictionary------------------\n-----------------------')

# ------------------------------
# Dictionary
# -----------------------------

person = {
    "name": "Alex",
    "age" : 22,
    "email" : "sam@gmail.com"
}
print(person["name"])
print(person.get("name"))
del person["name"]
print(person)
person["name"] = "jhon"
marks = {'c': 80,'python':90, 'C++':100}
ele = marks.pop('C++')
print(f'popped marks: {ele}')

res = marks.get('python')
print(res)

dict_keys = marks.keys()
print(dict_keys)

print(marks.values())