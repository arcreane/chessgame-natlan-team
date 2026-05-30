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
        return True   # temporary

    def askMove(self):
        return self.currentPlayer.askMove()

    def isCheckMate(self):
        return False   # temporary

    def updateBoard(self, move):
        # move format: "e2 e4"
        parts = move.split()

        if len(parts) != 2:
            return

        start = parts[0]
        end = parts[1]

        startPos = Position(start[0], int(start[1]))
        endPos = Position(end[0], int(end[1]))

        piece = self.board.getPiece(startPos)

        if piece is not None:
            piece.position = endPos

    def switchPlayer(self):
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
        else:
            self.currentPlayer = self.players[0]

    def play(self):
        self.initPlayers()

        while not self.isCheckMate():
            self.displayBoard()

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
