class Payment:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method

    def process_payment(self):
        print(f"Payment of {self.amount} processed via {self.payment_method}.")
