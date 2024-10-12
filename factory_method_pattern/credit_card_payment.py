from .payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paaid ${amount} to merchant using credit card')