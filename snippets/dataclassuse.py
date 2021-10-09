from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)

print(queen_of_hearts)

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')
                
queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts)