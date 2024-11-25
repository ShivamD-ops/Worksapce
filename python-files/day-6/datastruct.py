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