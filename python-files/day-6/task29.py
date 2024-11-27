def fun(num):
    if num == 1 or num == 0:
        return 1
    return num * fun(num-1)

for i in range(1,11):
    print(f"factorial of {i} is {fun(i)}")

# if ruccursion is wrong or missing base condition
# recursion will go on infinetly and stackoverflow error will occur
