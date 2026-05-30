from Piece import Piece
from position import Position

class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self):
        return "P"

    def isValidMove(self, newPosition, board):
        col = self.position.column
        row = self.position.row
        newCol = newPosition.column
        newRow = newPosition.row

        # White pawns move up (row increases), black pawns move down (row decreases)
        direction = 1 if self.color == 0 else -1

        # --- Normal move forward (1 square) ---
        if col == newCol and newRow == row + direction:
            # Square must be empty
            if board.getPiece(newPosition) is None:
                return True

        # --- First move: can move 2 squares forward ---
        startRow = 2 if self.color == 0 else 7
        if col == newCol and row == startRow and newRow == row + 2 * direction:
            # Both squares in between and destination must be empty
            middlePos = Position(col, row + direction)
            if board.getPiece(middlePos) is None and board.getPiece(newPosition) is None:
                return True

        # --- Diagonal capture ---
        if (newCol == chr(ord(col) + 1) or newCol == chr(ord(col) - 1)) and newRow == row + direction:
            target = board.getPiece(newPosition)
            # There must be an enemy piece there
            if target is not None and target.color != self.color:
                return True

        return False


if __name__ == "__main__":
    from position import Position
    from Board import Board

    board = Board()



    pawn = Pawn(Position("e", 2), 0)
    board.pieces.append(pawn)

    # Move forward 1
    print("e2 -> e3:", pawn.isValidMove(Position("e", 3), board))  # True
    # Move forward 2 from start
    print("e2 -> e4:", pawn.isValidMove(Position("e", 4), board))  # True
    # Move forward 3 (invalid)
    print("e2 -> e5:", pawn.isValidMove(Position("e", 5), board))  # False
    # Move sideways (invalid)
    print("e2 -> d2:", pawn.isValidMove(Position("d", 2), board))  # False
