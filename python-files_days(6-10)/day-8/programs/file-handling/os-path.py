import os
#getting current directory'
print(os.getcwd())
#creating new directory
# os.mkdir("demo")
#changing directory
os.chdir("demo")

#getting current directory
print(os.getcwd())

file = open('info.txt','w')
file.write("New File Line 1")
file.close()
file = open('info.txt','a')
file.write("\nNew File Line 2")
file.close()

file = open("info.txt","r")
print(file.read(),"\n---------------------------")

with open("info.txt","r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word,"\n")



