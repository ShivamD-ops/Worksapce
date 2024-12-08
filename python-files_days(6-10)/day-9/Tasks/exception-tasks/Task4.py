try:
    num = float(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
else:
    print(f"The result of 100 divided by {num} is {result}.")

'''

1) Multiple Except blocks helps to raise ultiple exceptions as different types of exception can occur to same code
2) when result is devided by 0 the devision by zero exception occurs
while when non numeric input code goes to valueError Block
3) we can add Overflow exception as->
except Overflow:
    print("")
    

'''