import random
from Player import Player

class AIPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)

    def askMove(self, board):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rows = [1, 2, 3, 4, 5, 6, 7, 8]
        
        col1 = random.choice(columns)
        row1 = random.choice(rows)
        col2 = random.choice(columns)
        row2 = random.choice(rows)
        
        return f"{col1}{row1} {col2}{row2}"
