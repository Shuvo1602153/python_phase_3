class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance        #privet style attribute

    def deposit(self,amount):
        if amount < 0:
            print("Amount cannot be negative!")
            return
        self.__balance += amount
    def get_balance(self):
        return self.__balance

acc1 = BankAccount("Shuvo",150000)
print(acc1.get_balance())
acc1.deposit(40000)
print(acc1.get_balance())

