from functools import reduce, partial
from operator import add, mul, itemgetter, methodcaller
import random

# functions are first-class objects


def factorial(n):
    """Returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(4))
print(factorial.__doc__)
print(type(factorial))

fact = factorial
print(fact(4))
print(fact)

print(list(map(fact, range(4))))

# map, filter, reduce, apply - higher order funcs (take other funcs as an input)


def rev(word):
    return word[::-1]


fruits = ['apple', 'banana', 'orange', 'grapes']

print(sorted(fruits, key=rev))
print(sorted(fruits, key=lambda word: word[::-1]))  # anonymous function

print(list(map(fact, range(4))))
print([fact(n) for n in range(4)])

print(list(map(fact, filter(lambda n: n % 2, range(4)))))
print([fact(n) for n in range(4) if n % 2])


print(reduce(add, range(100)))
print(sum(range(100)))


# To check if obj is callable, use callable
a = 1
print(callable(a))

def a():
    print(10)

print(callable(a))

# To make class instance callable, add __call__ method


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(2))
print(bingo.pick())
print(bingo())


print(dir(fact))


def f(a, *, b):  # this will make b passed only as named argument
    return a, b


print(f(1, b=2))


def f(a, b=7):
    return a, b


print(f.__defaults__)
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)


def f(a: str, b: 'int > 0' = 7) -> (str, 'int > 0'):  # this will make b passed only as named argument
    return a, b


print(f.__annotations__)

metro_data = [('Tokyo', 'Japan', 4, 63),
              ('New York', 'America', 5, 95),
              ('Kyiv', 'Ukraine', 6, 74)]

print(sorted(metro_data, key=itemgetter(1)))  # itemgetter(1) - same as lambda x: x[1]


cc_name = itemgetter(0, 1)
for city in metro_data:
    print(cc_name(city))


upcase = methodcaller('upper')
print(upcase('i love python'))

upcase = methodcaller('replace', ' ', '-')
print(upcase('i love python'))

triple = partial(mul, 3)
print(triple(5))
print([triple(n) for n in range(6)])
