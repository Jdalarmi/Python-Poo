from .payment import Payment

class GooglePayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paaid ${amount} to merchant using google')