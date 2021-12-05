class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    # withdrawal method
    def make_withdrawal(self,amount): # takes an argument that is the amount to withdraw
        if self.account_balance - amount >= 0: # Only decrement account if result is greater than 0
            self.account_balance -= amount # the specific user's account decremented by the amount of the value received
        else:
            print(f"Cannot withdraw {amount} from account with balance {self.account_blance}.")
    # display balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    # transfer
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
    



guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
limp = User("Limp Bizkit", "limp@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(45)

guido.display_user_balance() # 305 Balance

monty.make_deposit(1000)
monty.make_deposit(2000)
monty.make_withdrawal(2000)
monty.make_withdrawal(500)

monty.display_user_balance() # 500 Balance

limp.make_deposit(1000)
limp.make_withdrawal(300)
limp.make_withdrawal(200)
limp.make_withdrawal(200)

limp.display_user_balance() # 300 Balance

guido.transfer_money(limp,299)




