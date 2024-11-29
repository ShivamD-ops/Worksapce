# List Comprehenssion
# [Expression for item in list if condition]
numbers = [10,11,12,13]

doubled_numbers = [num * 2 for num in numbers]

print(f"{doubled_numbers} with list comprehenssion")


squared_numbers = []

for i in numbers:
    squared_numbers.append(i*i)

squared_numbers1 = [i*i for i in numbers]

print(f"{squared_numbers} without list commprehenion")
print(f"{squared_numbers1} with list commprehenion")


