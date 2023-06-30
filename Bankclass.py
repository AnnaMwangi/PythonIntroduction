class BankAccount:
    def __init__(self, account_number, holder_name, account_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("insufficient funds")

    def display_balance(self):
        print(f"Account Number:{self.account_number}")
        print(f"Holder name:{self.holder_name}")
        print(f"Account Balance:{self.account_balance}")


my_account = BankAccount("1234567", "Ann", 1000)
my_account.display_balance()
my_account.deposit(500)
my_account.display_balance()
my_account.withdrawal(2000)
