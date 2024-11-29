try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result is: {result}")
'''
1) when we tried to devide a number by 0 ZeroDivisionError exception occured
2) As we handled exception correctly code countinues to follow after the print of exception
3) If we remove exception block code terminates abruptly

'''
