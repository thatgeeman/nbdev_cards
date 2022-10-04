# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_cards.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_cards.ipynb 2
from fastcore.utils import patch

# %% ../nbs/00_cards.ipynb 4
suits = "♠♥♣♦"
ranks = [None, 'A'] + [str(x) for x in range(2, 11)] + ['J', 'Q', 'K']

# %% ../nbs/00_cards.ipynb 12
class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
    def __str__(self) -> str:
        return f'{ranks[self.rank]} {suits[self.suit]}'
    def __repr__(self) -> str:
        return self.__str__()
    

# %% ../nbs/00_cards.ipynb 15
@patch
def __eq__(self: Card, other:Card):
    return (self.suit == other.suit) and (self.rank == other.rank)

@patch
def __lt__(self: Card, other:Card):
    return (self.suit < other.suit) and (self.rank < other.rank)

@patch
def __gt__(self: Card, other:Card):
    return (self.suit > other.suit) and (self.rank > other.rank)