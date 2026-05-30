class King(Piece):
    def is_valid_move(self, new_position, board):

        dx = abs(new_position.row - self.position.row)
        dy = abs(new_position.column - self.position.column)

        return dx <= 1 and dy <= 1 and not (dx == 0 and dy == 0)
