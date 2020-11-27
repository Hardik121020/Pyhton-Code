class Account:
    def __init__(self,initial_account):
        self.balance = initial_account
    def withdraw(self,amount):
        self.balance = self.balance - amount
    def deposit(self,amount):
        self.balance = self.balance + amount
acc = Account(3000)

acc.balance = 2000
acc.balance = -1000
print(acc.balance)


acc1 = Account(3000)
acc1.deposit(2000)
acc1.withdraw(1000)
print(acc1.balance)
