# class BkashPaymeny:
   
#     def payment(self, amount):
#         self.amount = amount
#         print("Pay through Bkash\n")

# class CardPayment:
    
#     def payment(self, amount):
#         self.amount = amount
#         print("Pay through Bkash\n")

# payments = [BkashPaymeny(), CardPayment()]

# # for method in payments:
# #     method.payment(500)

# BkashPaymeny().payment(500)

class SavingsAccount:
    def __init__(self,author,balance):
        self.author =author
        self.balance = balance
    def withdraw(self,amount):
        if amount > 50000:
            print("Your limit is exceeded!")
            return
        if amount > self.balance:
            print("Not enough balance!")
            return
        self.balance -= amount
        print(f"Savings account balance is {self.balance}") 
class CurrentAccount:
    def __init__(self,author,balance,overdraft_limit = 10000):
        self.author = author
        self.balance = balance
        self.overdraft_limit = overdraft_limit 
    def withdraw(self,amount):
        if amount > self.balance + self.overdraft_limit:
            print("Your limit is exceeded!")
            return
        self.balance -= amount
        print(f"Curent account balance is {self.balance}")

accounts = [
    SavingsAccount("shuvo", 50000),
    CurrentAccount("Ripa",35000)
]

for acc in accounts:
    acc.withdraw(50000)
        