class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    accounts = []
    def __init__(self, account_name, int_rate, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        if self.account_type == type:
            self.balance += amount
        return self

    def withdraw(self, amount, account_name):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

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
        self.account = BankAccount(.02,1000)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        
    def make_withdrawal(self,amount): 
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.display_account_info}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()

guido = User("Guido Sarduchi", "guido@python.com")


