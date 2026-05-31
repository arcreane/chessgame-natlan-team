class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self):
        return "K"

    def isValidMove(self, newPosition, board):
        dx = abs(newPosition.row - self.position.row)
        dy = abs(ord(newPosition.column) - ord(self.position.column))

        if dx == 0 and dy == 0:
            return False

        if not (dx <= 1 and dy <= 1):
            return False

        target = board.getPiece(newPosition)
        if target is not None and target.color == self.color:
            return False

        return True
