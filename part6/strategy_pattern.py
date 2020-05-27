from abc import ABC
from abc import abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context of pattern
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # the Strategy of pattern: abstract base class
    @abstractmethod
    def discount(self, order):
        """Return discount"""


class FidelityPromo(Promotion):
    """5%"""
    def discount(self, order):  # first concrete Strategy
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):  # second concrete Strategy
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order):  # third concrete Strategy
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


joe = Customer('John', 0)
ann = Customer('Ann', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, BulkItemPromo()))
print(Order(ann, banana_cart, BulkItemPromo()))

long_cart = [LineItem(str(i), 1, 1.0) for i in range(10)]

print(Order(joe, long_cart, LargeOrderPromo()))
print(Order(ann, long_cart, BulkItemPromo()))
