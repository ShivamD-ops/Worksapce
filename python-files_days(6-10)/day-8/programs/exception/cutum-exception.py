try:
    even_nums = [2,4,6,8]
    print(even_nums[5])
except ZeroDivisionError:
    print("Denomenator cannot be 0")
except IndexError:
    print("Index out of bound")

# ///////////////////////////
# Assert - used
# //////////////////////////
try: 
    num = int(input('Enter a number :'))
    assert num % 2 == 0
except:
    print("Not an Even Number !!")
else:
    reciprocal = 1/num
    print(reciprocal)