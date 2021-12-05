class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    # deposit method
    def make_deposit(self, amount):	
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    # withdrawal method
    def make_withdrawal(self,amount): # takes an argument that is the amount to withdraw
        if self.account_balance - amount >= 0: # Only decrement account if result is greater than 0
            self.account_balance -= amount # the specific user's account decremented by the amount of the value received
        else:
            print(f"Cannot withdraw {amount} from account with balance {self.account_blance}.")
        return self
    # display balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    # transfer money
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
        return self
    

guido = User("Guido van Rossum")
monty = User("Monty Python")
limp = User("Limp Bizkit")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(45).display_user_balance() # 305 Balance

monty.make_deposit(1000).make_deposit(2000).make_withdrawal(2000).make_withdrawal(500).display_user_balance() # 500 Balance

limp.make_deposit(1000).make_withdrawal(300).make_withdrawal(200).make_withdrawal(200).display_user_balance() # 300 Balance

guido.transfer_money(limp,299)




