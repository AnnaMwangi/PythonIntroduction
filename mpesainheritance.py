class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class DepositTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Deposit Transaction with ID{self.transaction_id}processed.Amount{self.amount}")


class WithdrawalTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Withdrawal transaction with ID{self.transaction_id}processed.Amount{self.amount}processed")


class PaymentTransaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recepient):
        super().__init__(transaction_id, amount, )
        self.recepient = recepient

    def process_transaction(self):
        print(
            f"Payment transaction with ID{self.transaction_id}processed.Amount{self.amount}Recipient{self.recepient}processed")
class LoanTransaction(MpesaTransaction):
    def process_transaction(self):
        print(f"Loan transaction with ID{self.transaction_id}processed.Amount{self.amount}processed")

deposit = DepositTransaction("DHTY", 2000)
withdrawal = WithdrawalTransaction("ARTH", 3000)
payment = PaymentTransaction("RJIK", 4000, "Anna")
Loan=LoanTransaction("YTHI",7000)
deposit.process_transaction()
withdrawal.process_transaction()
payment.process_transaction()
Loan.process_transaction()
