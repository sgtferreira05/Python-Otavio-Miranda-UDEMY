# namedtuples - imutables tuples avec names to values
# We employ namedtuples to construct object classes that serve solely as attribute containers, analogous to regular classes devoid of methods, or databases records, etc.
# The namedtuples are imutables such as the tuples


# from collections import namedtuple

# Card = namedtuple('Card', ['value', 'suit'],
#                   defaults=['VALUE', 'SUIT']
# )
# spades_as = Card('A', '♠️')
# print(spades_as)
# print(spades_as.value, spades_as.suit)
# print()
# print(spades_as._fields)
# print(spades_as._field_defaults)
# print()
# print(spades_as._asdict())

##################################

from typing import NamedTuple
class Card(NamedTuple):
    value: str = 'VALUE'
    suit: str = 'SUIT'

spades_as = Card('A', '♠️')
print(spades_as)