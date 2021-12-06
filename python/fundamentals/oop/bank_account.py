class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

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
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

    # class method to get balances of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            account.display_account_info()
        return sum

    # static method have no access to any attribute only to what is passed into it
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

account1 = BankAccount(.01)
account2 = BankAccount(.02,10000)

account1.deposit(10000).deposit(2340).deposit(1200).withdraw(5000).yield_interest().display_account_info()
account2.deposit(210).deposit(720).withdraw(100).withdraw(200).withdraw(300).withdraw(120).yield_interest().display_account_info()

BankAccount.all_balances()