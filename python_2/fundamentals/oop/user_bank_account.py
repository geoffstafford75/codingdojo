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


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "Checking" : BankAccount(.02, 0),
            "Savings" : BankAccount(.05, 0)
        }
    # adding the deposit method
    def make_deposit(self, name, amount):	# takes an argument that is the amount of the deposit
        self.account[name].balance += amount	# the specific user's account increases by the amount of the value received
        return self
    # withdrawal method
    def make_withdrawal(self, name, amount): # takes an argument that is the amount of the withdrawal
        self.account[name].balance -= amount
        return self
    # display balance
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['Checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['Savings'].display_account_info()}")
        return self
    # transfer money
    def transfer_money(self, other_user, name, amount):
        self.make_withdrawal(name,amount)
        other_user.make_deposit(name,amount)
        self.display_user_balance()
        other_user.display_user_balance()
        return self

guido = User("Guido Sarduchi", "guido@python.com")
guido.make_deposit("Checking",5000).display_user_balance()

