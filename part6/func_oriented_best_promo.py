import part6.strategies
import inspect
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
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
            discount = self.promotion(self)  # pass order to a function

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# get all function names in strategies module - no need to add elements to promos
# promos = [globals()[name] for name in globals() if name.endswith('_promo')]
promos = [func for name, func in inspect.getmembers(part6.strategies, inspect.isfunction)]


def best_promo(order):
    return max(promo(order) for promo in promos)


joe = Customer('John', 0)
ann = Customer('Ann', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]

print(best_promo(Order(joe, cart)))
print(best_promo(Order(ann, cart)))
