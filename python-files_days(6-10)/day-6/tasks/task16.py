str1 = "shivam"
str2 = str1.upper()
str3 = str1.lower()
str4 = str1.replace("s","h")
print(f'original String -> {str1}',f'upper() -> {str2}', f'lower()-> {str3}', f'repace("s","h")-> {str4}')

# 2
res = str1 + " " + str2
# Use + to concat strings
print(res)

# slicing
# we can use [:] to slice a substring
str1 = str1[:5]
print(str1)

# slicing index out of range->
str2 = str2[:9]
print(str2)
# it goes till last index and return full string