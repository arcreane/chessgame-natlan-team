class Piece:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def isValidMove(self, newPosition, board):
        return True   # temporary

    def __str__(self):
        return "?"

if __name__ == "__main__":
    from position import Position

    pos = Position("e", 2)
    piece = Piece(pos, 0)

    print("Piece created at:", piece.position)
    print("Piece symbol:", piece)

    print("Test Piece OK!")
