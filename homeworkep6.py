class Account:
    
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'deposit {amount}')
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'Withdraw {amount}')
        else :
            print('Not enough')
    def showbalance(self):
        print(f'Balance {self.balance}')

class Customer(Account):
    
    def __init__(self,fName, balance):
        super().__init__(balance)
        self.fName = fName
        print(f'Bank Account : {self.fName}')

account01 = Customer('Jedsada Chanmanee' , 5000)
account01.deposit(5000)
account01.withdraw(2000)
account01.showbalance()