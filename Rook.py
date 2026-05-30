from Piece import Piece
from jade_path_clear import path_clear, COLUMNS


class Rook(Piece):
    def isValidMove(self, newPosition, board) -> bool:
        if self.position.column == newPosition.column and self.position.row == newPosition.row:
            return False

        target = board.getPiece(newPosition)
        if target is not None and target.color == self.color:
            return False

        rs = self.position.row
        cs = COLUMNS.index(self.position.column)
        re = newPosition.row
        ce = COLUMNS.index(newPosition.column)

        if rs != re and cs != ce:
            return False

        dr = 0 if rs == re else (1 if re > rs else -1)
        dc = 0 if cs == ce else (1 if ce > cs else -1)

        if not path_clear(board, self.position, newPosition, dr, dc):
            return False

        return True

    def __str__(self):
        return "R" if self.color == 0 else "r"