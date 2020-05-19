from random import choice
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


beer_card = Card('7', 'diamonds')
print(beer_card)
print(beer_card.rank)
print(beer_card.suit)

deck = FrenchDeck()

print(len(deck))  # __len__

print(deck[0])  # __getitem__
print(deck[-1])

print(choice(deck))  # __getitem__ + __len__ lets us use choice()
print(choice(deck))
print(choice(deck))

print(deck[:3])  # __getitem__
print(deck[11:13])
print(deck[11::13])


for card in deck[:5]:  # __getitem__ makes it iterable
    print(card)

print(Card('Q', 'spades') in deck)  # if a collection has no __contains__ - "in" will perform sequential scan
print(Card('Q', 'lol') in deck)

# By implementing __getitem__ + __len__ methods class behaves as a standard python sequence!
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high)[:5]:
    print(card)

print(len(deck))  # python interpreter calls __len__() for us
print(deck.__len__())


