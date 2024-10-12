from .payment import Payment

class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f'Successfuly paaid ${amount} to merchant using pay pal')