from inspect import getmembers, isclass, isabstract
import factory_method_pattern


class PaymentFactory(object):
    payment_implementations = {}

    def __init__(self):
        self.load_payment_methods()

    def load_payment_methods(self):
        implementations = getmembers(factory_method_pattern, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, factory_method_pattern.Payment):
                self.payment_implementations[name] = _type

    def create(self, payment_type: str):
        if payment_type in self.payment_implementations:
            return self.payment_implementations[payment_type]()

        raise ValueError(f"{payment_type} payment type not supported")