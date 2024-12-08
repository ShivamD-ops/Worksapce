#python String
msg = "Learning Python"
print(msg)

msg1 = "Python is a Programming Language"
print(msg,msg1)

greet = 'Welcome'

print(greet[1])
print(greet[-6]) #Negative Indexing
print(greet[2:5]) #slicing

#string is immutable does not support item asignment
# multiline string
msg2 = """ 
    Learning Python is Fun
    and its useful
 """

msg3 = ''' 
    Python
    is
    a
    Programming
    laguage
'''
print(msg2,msg3)

print(msg2 != msg3) #-> True
s1 = 'Hello'
s2 = 'Hello'
print(s1 == s2) # -> True

#Concat -> use +
print(s1 + " " + s2)