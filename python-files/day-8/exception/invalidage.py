class InvalidAgeException(Exception):
    pass
number = 18
try:
    input_num = int(input("Enter a number : "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligigble to vote")
except InvalidAgeException as e:
    print(e,"Exception Occured: Invalid Age")