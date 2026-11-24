from abc import ABC , abstractmethod

class Account(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass

class DemoAccount(Account):
    def withdraw(self, amount):
        print(f"Withdraw {amount}")
        
acc= DemoAccount()
acc.withdraw(1000)