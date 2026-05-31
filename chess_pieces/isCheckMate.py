def isCheckMate(self):

    king = None

    # find current player's king
    for piece in self.board.pieces:
        if isinstance(piece, King) and piece.color == self.currentPlayer.color:
            king = piece
            break
        print("CHECKMATE FUNCTION WORKING")

    if king is None:
        return False

    # check if any enemy piece can attack king
    for piece in self.board.pieces:

        if piece.color != king.color:

            if piece.isValidMove(king.position, self.board):
                return True

    return False
    
