from Piece import Piece

class Queen(Piece):
    def __init__(self, position,color):
        super().__init__(position,color)

    def __str__(self):
        return "Q"

    def isValidMove(self, newPosition, board):
        current_col = ord(self.position.column) - ord('a')
        current_row = self.position.row
        new_col = ord(newPosition.column) - ord('a')
        new_row = newPosition.row

        col_diff = new_col - current_col
        row_diff = new_row - current_row

        is_horizontal = row_diff == 0 and col_diff != 0
        is_vertical = col_diff == 0 and row_diff != 0
        is_diagonal = abs(col_diff) == abs(row_diff)

        if not (is_horizontal or is_vertical or is_diagonal):
            return False

        col_step = 0 if col_diff == 0 else (1 if col_diff > 0 else -1)
        row_step = 0 if row_diff == 0 else (1 if row_diff > 0 else -1)

        check_col = current_col + col_step
        check_row = current_row + row_step

        while check_col != new_col or check_row != new_row:
            from position import Position
            middle_pos = Position(chr(check_col + ord('a')), check_row)
            if board.getPiece(middle_pos) is not None:
                return False
            check_col += col_step
            check_row += row_step

        piece_at_destination = board.getPiece(newPosition)
        if piece_at_destination is not None and piece_at_destination.color == self.color:
            return False

        return True
    def __str__(self):
        return "Q" if self.color == 0 else "q"
