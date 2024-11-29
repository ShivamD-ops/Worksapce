try:
    age = int(input("Enter your age: "))
    assert age > 0, "Age must be a positive number."
except AssertionError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"Your age is {age}.")
'''
1) Assert raises an exception as the condition is not satisfied
2) If non Numeric value is input ValueError Exception will occur
3) except AssertionError as e: handles the Assertion Error as assert condition gives False

'''