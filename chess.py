from Board import Board
from Player import Player
from position import Position


class Chess:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.currentPlayer = None

    def initPlayers(self):
        from AIPlayer import AIPlayer

        name1 = input("Enter name for Player 1: ")
        name2 = input("Enter name for Player 2: ")

        p1 = AIPlayer(name1, 0) if name1 == "AI" else Player(name1, 0)
        p2 = AIPlayer(name2, 1) if name2 == "AI" else Player(name2, 1)

        self.players = [p1, p2]
        self.currentPlayer = p1

    def displayBoard(self):
            print("\n    a  b  c  d  e  f  g  h")
            print("   ------------------------")

            for row in range(8, 0, -1):
                print(f"{row} |", end=" ")
                for col in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                    piece = self.board.getPiece(Position(col, row))
                    if piece is None:
                        print(".", end="  ")
                    else:
                        print(str(piece), end="  ")
                print(f"| {row}")

            print("   ------------------------")
            print("    a  b  c  d  e  f  g  h\n")

    def isValidMove(self, move):
        parts = move.split()
        if len(parts) != 2:
            return False

        start = parts[0]
        end = parts[1]

        # validate format
        if len(start) != 2 or len(end) != 2:
            return False

        startPos = Position(start[0], int(start[1]))
        endPos = Position(end[0], int(end[1]))

        # find the piece at start position
        piece = self.board.getPiece(startPos)

        if piece is None:
            print("No piece at that position!")
            return False

        # check it belongs to current player
        if piece.color != self.currentPlayer.color:
            print("That's not your piece!")
            return False

        # call the piece's own isValidMove
        return piece.isValidMove(endPos, self.board)

    def askMove(self):
        return self.currentPlayer.askMove()

    def isInCheck(self, color):
        king = None
        for piece in self.board.pieces:
            if piece.__str__() == "K" and piece.color == color:
                king = piece
                break
            if piece.__str__() == "k" and piece.color == color:
                king = piece
                break


        if king is None:
            return False

        for piece in self.board.pieces:
            if piece.color != color:
                if piece.isValidMove(king.position, self.board):
                    return True

        return False

    def isCheckMate(self):
        color = self.currentPlayer.color
        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

        if not self.isInCheck(color):
            return False

        for piece in self.board.pieces:
            if piece.color != color:
                continue

            for col in columns:
                for row in range(1, 9):
                    newPos = Position(col, row)

                    if not piece.isValidMove(newPos, self.board):
                        continue

                    originalPos = piece.position
                    capturedPiece = self.board.getPiece(newPos)

                    piece.position = newPos
                    if capturedPiece is not None:
                        self.board.pieces.remove(capturedPiece)

                    stillInCheck = self.isInCheck(color)

                    piece.position = originalPos
                    if capturedPiece is not None:
                        self.board.pieces.append(capturedPiece)

                    if not stillInCheck:
                        return False

        return True

    def updateBoard(self, move):
        parts = move.split()

        if len(parts) != 2:
            return

        start = parts[0]
        end = parts[1]

        startPos = Position(start[0], int(start[1]))
        endPos = Position(end[0], int(end[1]))

        piece = self.board.getPiece(startPos)
        target = self.board.getPiece(endPos)

        # Remove captured piece from board
        if target is not None:
            self.board.pieces.remove(target)

        if piece is not None:
            piece.position = endPos
    def switchPlayer(self):
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
        else:
            self.currentPlayer = self.players[0]

    def play(self):
        self.initPlayers()

        while True:
            self.displayBoard()

            
            kingFound = any(str(p) in ["K", "k"] and p.color == self.currentPlayer.color
                            for p in self.board.pieces)
            if not kingFound:
                print(f"Game Over! {self.currentPlayer.name} lost!")
                break


            if self.isCheckMate():
                print(f"Checkmate! {self.currentPlayer.name} lost!")
                break

            move = self.askMove()

            if move == "exit":
                print("Game over")
                break

            if self.isValidMove(move):
                self.updateBoard(move)
                self.switchPlayer()

        print("Game Over!")



if __name__ == "__main__":
    print("STARTING CHESS TEST")

    game = Chess()
    game.play()
