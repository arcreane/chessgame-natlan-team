from position import Position
from Piece import Piece
# Import all piece types
from pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from queen import Queen
from King import King


class Board:
    def __init__(self):
        self.pieces = []
        self._setupPieces()

    def _setupPieces(self):
        # Dictionary mapping piece type name -> class
        # (this is required dictionary from the spec!)
        pieceClasses = {
            "Rook": Rook,
            "Knight": Knight,
            "Bishop": Bishop,
            "Queen": Queen,
            "King": King,
            "Pawn": Pawn,
        }

        # Back row order for both sides
        backRow = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # White back row (row 1) and pawns (row 2)
        for i, pieceName in enumerate(backRow):
            cls = pieceClasses[pieceName]
            self.pieces.append(cls(Position(columns[i], 1), 0))  # white
        for col in columns:
            self.pieces.append(Pawn(Position(col, 2), 0))  # white pawns

        # Black back row (row 8) and pawns (row 7)
        for i, pieceName in enumerate(backRow):
            cls = pieceClasses[pieceName]
            self.pieces.append(cls(Position(columns[i], 8), 1))  # black
        for col in columns:
            self.pieces.append(Pawn(Position(col, 7), 1))  # black pawns

    def getPiece(self, position):
        for piece in self.pieces:
            if (piece.position.column == position.column and
                    piece.position.row == position.row):
                return piece
        return None

    def getPosition(self, piece):
        return piece.position


if __name__ == "__main__":
    board = Board()

    print("Total pieces:", len(board.pieces))  # Should be 32

    # Test a few starting positions
    print("e1:", board.getPiece(Position("e", 1)))  # King (white)
    print("e8:", board.getPiece(Position("e", 8)))  # King (black)
    print("a2:", board.getPiece(Position("a", 2)))  # Pawn (white)
    print("d1:", board.getPiece(Position("d", 1)))  # Queen (white)
    print("e5:", board.getPiece(Position("e", 5)))  # None (empty)
