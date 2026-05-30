from Piece import Piece

class Knight(Piece):
    def __init__(self,position,color):
        self.color = color
        self.position = position

    def __str__(self):
        return "N"

    def isValidMove(self, newPosition, board):
        current_col = ord(self.position.column) - ord('a')
        current_row = self.position.row
        new_col = ord(newPosition.column) - ord('a')
        new_row = newPosition.row
        col_diff = abs(new_col - current_col)
        row_diff = abs(new_row - current_row)
        if not ((col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)):
            return False
        piece_at_destination = board.getPiece(newPosition)
        if piece_at_destination is not None and piece_at_destination.color == self.color:
            return False
        return True