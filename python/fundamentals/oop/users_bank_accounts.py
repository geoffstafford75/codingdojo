class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=5
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    @classmethod
    def all_balances(cls):
        sum = 0

        for account in cls.accounts:
            account.display_account_info()
        return sum

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "Checking" : BankAccount(.02, 2000),
            "Savings" : BankAccount(.05, 3000)
        }
    
    def make_deposit(self, name, amount):
        print(name)
        self.account[name].deposit(amount)
        return self
        
    def make_withdrawal(self, name, amount): 
        self.account[name].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['Checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['Savings'].display_account_info()}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
        return self

guido = User("Guido Sarduchi", "guido@python.com")
guido.make_deposit("Checking",5000)
guido.display_user_balance()

