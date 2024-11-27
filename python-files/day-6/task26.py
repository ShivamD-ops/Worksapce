square = lambda x: x**2
list1 = list(map(square,[i for i in range(1,11)]))
#create a lambda function
# use map(lambda_func,list) to get list of elements with lambda applied to each element

print(list1, " created using lambda function")

# Not DEclared With name
# Can only contain a singe Expression
# Simple Single purpose functionality