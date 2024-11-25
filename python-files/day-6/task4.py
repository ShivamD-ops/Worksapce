n = int(input("Enter your marks"))
if n > 100 or n < 0:
    print("Invalid Input")
else :
    grade = "F"
    if n > 90:
        grade = "A"
    elif n > 70:
        grade = "B"
    elif n > 50:
        grade = "C"
    else :
        grade = "F"
    print(f'your grade is {grade}')

# Check if score invalid at input only