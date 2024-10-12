from payment_factory import PaymentFactory

factory = PaymentFactory()
payment = factory.create("ApplePay")
payment.pay(1000.00)