from bank_account import BankAccount #from file, import the class

account1 = BankAccount("123", 100)
print(account1)
account1.deposit(50)
print(account1)

account2 = BankAccount("122", 50)
print(account2)
account2.withdraw(25)
account2.get_balance()
