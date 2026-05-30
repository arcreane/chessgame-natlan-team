class Chess:
    def __init__(self, board):
        self.board = board

    def isCheckMate(self, king):

        for piece in self.board.pieces:

            if piece.color != king.color:

                if piece.is_valid_move(king.position, self.board):
                    return True

        return False