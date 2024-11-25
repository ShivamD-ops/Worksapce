dict1 = {
    "name" : "Shivam",
    "Age" : 23,
    "location": "Gurugram"
}
print(dict1)
dict1["job"] = "FrontEnd Devloper"
print(dict1)
dict1["age"] = 22
print(dict1)
del dict1["location"]
print(dict1)

# print(dict1["location"])
# If we try to access a key which is not present in the dictionary 
# then we get
# "KeyError: 'location'"