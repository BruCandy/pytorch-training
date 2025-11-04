class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest_rate = 0.01
    
    def deposit(self, value):
        self.balance += value
    
    def withdraw(self, value):
        self.balance -= value
    
    def get_balance(self):
        return self.balance
    
    def set_interest_rate(self, value):
        self.interest_rate = value

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate