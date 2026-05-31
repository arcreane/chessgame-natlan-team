def isCheckMate(self):

    king = None

    for piece in self. board.pieces:
        if isinstance(piece, King) and piece.color == self.currentPlayer.color:
            King = piece
            break

    if king is None:
        return False

    for piece in self. board.pieces:
        if piece.color != king.color:
            if piece.isValidMove(king.position, self.board):
                return True

    return False
