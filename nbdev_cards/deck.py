# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 2
from .card import Card
from fastcore.utils import L, patch

# %% ../nbs/01_deck.ipynb 4
class Deck:
    "Class to store a deck of Cards"
    def __init__(self) -> None:
        self.cards = L([Card(s, r) for s in range(0,4) for r in range(1, 14)])
    
    def __len__(self) -> int:
        "Returns length of the deck"
        return len(self.cards)
    
    def __str__(self) -> str:
        return ", ".join([str(c) for c in self.cards])
    
    def __repr__(self) -> str:
        return self.__str__()
    

# %% ../nbs/01_deck.ipynb 10
@patch
def pop(self:Deck,  # Deck of Cards
            idx=-1  # index to pop, default -1
            ) -> Deck:
    "Pop an item from the deck"
    return self.cards.pop(idx)

# %% ../nbs/01_deck.ipynb 13
@patch
def shuffle(self:Deck,  # `Deck` of `Card``
            seed=42  # random seed
            ) -> Deck:
    "Shuffle the Deck"
    return self.cards.shuffle()
