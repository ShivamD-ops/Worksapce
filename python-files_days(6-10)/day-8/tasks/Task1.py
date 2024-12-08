class InvalidDeposit(Exception):
    pass
class InvalidWithdraw(Exception):
    pass
class BankerAccount:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.__balance = 0.0

    def deposit(self,amount):
        try:
            if amount > 0:
                self.__balance += amount
                print(f"deposited {amount} in {self.account_holder}'account current balance is {self.get_balance()}")
            else:
                raise InvalidDeposit
        except InvalidDeposit:
            print("Invalid deposit request")

    def withdraw(self,amount):
        try:
            if amount > self.__balance:
                raise InvalidWithdraw
            self.__balance -= amount
            print(f"Withdraw of {amount} in {self.account_holder}'account current balance is {self.get_balance()}")
            
        except Exception as e:
            print(f"Exception {e} occured, Invalid withdraw")
    def get_balance(self):
        balance = self.__balance
        return balance
    def get_name(self):
        return self.account_holder

acc1 = BankerAccount("Jhon Doe")
print(f"current balance of {acc1.get_name()} is {acc1.get_balance()}")

acc1.deposit(500.0)
acc1.withdraw(10)
acc1.deposit(10000)
acc1.withdraw(5000)
acc1.withdraw(2000)
acc1.deposit(3000)
print(f"{acc1.__balance}")

# Ques1# -> AttributeError: 'BankerAccount' object has no a
# ttribute '__balance'. Did you mean: 'get_balanc
# e'?
# Encapsulation protects the private data from being
# accessed from outside

# Question 2 
'''
We will  use try: except: to raise an exception
also we will make class of exception with our custom 
name who will inherit fom Eception class
class InvalidDeposit(Exception):
    pass
class InvalidWithdraw(Exception):
    pass

'''