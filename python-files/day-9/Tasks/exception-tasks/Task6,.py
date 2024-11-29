class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Please enter your age: "))
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"Your age is {age}.")
'''
1) Raising a custom exception like InvalidAgeError can allow customization on logical errors which are useful and known to the application
2) We use Raise keyword under the if block to raise custom exception
3) Errors can be handled in a better way as logical exception only unique to applixation help in 
improving error handling when we have freedom of creating custom exceptions
'''