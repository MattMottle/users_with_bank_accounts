class Savings:
    def __init__(self, savings_int_rate, savings_balance): 
        self.savings_balance = savings_balance
        self.savings_int_rate = savings_int_rate
    
    def deposit_savings(self, amount):
        self.savings_balance = self.savings_balance + amount
        return self
    
    def withdraw_savings(self, amount):
        if amount > self.savings_balance:
            print("Insufficient funds: Charging a $5 fee")
            self.savings_balance = self.savings_balance - 5
        else:
            self.savings_balance = self.savings_balance - amount
        return self
    
    def display_savings_info(self):
        print(f"Savings Balance: {self.savings_balance}")
        print(f"Savings Interest: {self.savings_int_rate}")
        return self
    
    def yield_interest_savings(self):
        interest = self.savings_balance * self.savings_int_rate
        self.savings_balance = self.savings_balance + interest
        return self

class Checking:
    def __init__(self, checking_int_rate, checking_balance): 
        self.checking_balance = checking_balance
        self.checking_int_rate = checking_int_rate
    
    def deposit_checking(self, amount):
        self.checking_balance = self.checking_balance + amount
        return self
    
    def withdraw_checking(self, amount):
        if amount > self.checking_balance:
            print("Insufficient funds: Charging a $5 fee")
            self.checking_balance = self.checking_balance - 5
        else:
            self.checking_balance = self.checking_balance - amount
        return self
    
    def display_checking_info(self):
        print(f"Checking Balance: {self.checking_balance}")
        print(f"Checking Interest: {self.checking_int_rate}")
        return self
    
    def yield_interest_checking(self):
        interest = self.checking_balance * self.checking_int_rate
        self.checking_balance = self.checking_balance + interest
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings_account = Savings(savings_int_rate=0.02, savings_balance=0)
        self.checking_account = Checking(checking_int_rate=0.01, checking_balance=0 )
    
    def make_deposit_savings(self, amount):
        self.savings_account.deposit_savings(amount)
        return self

    def make_withdrawal_savings(self, amount):
        self.savings_account.withdraw_savings(amount)
        return self
    
    def make_deposit_checking(self, amount):
        self.checking_account.deposit_checking(amount)
        return self

    def make_withdrawal_checking(self, amount):
        self.checking_account.withdraw_checking(amount)
        return self
    
    def display_user_balance(self):
        print(f"Account: {self.name}")
        self.savings_account.display_savings_info()
        self.checking_account.display_checking_info()
        return self


matt = User("Matt Mottle", "mattmottle@codingdojo.com")
brad = User("Brad", "brad@codingdojo.com")

matt.make_deposit_checking(100).make_deposit_savings(100).make_withdrawal_checking(50).make_withdrawal_savings(24).display_user_balance()
brad.make_deposit_checking(1000).make_deposit_savings(5000).display_user_balance()