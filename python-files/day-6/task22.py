class Calculator:
    def __init__(self):
        pass
    @staticmethod
    def add(a,b):
        return a + b 
print("Sum of 4 and 11 ->",Calculator.add(4,7))

# Difference b/w staticmethod and instance method is that 
# staticmethod does not require an object to be created to be called
