class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def askMove(self):
        move = input(f"{self.name}, enter your move: ")
        return move


if __name__ == "__main__":
    print("RUNNING PLAYER TEST")

    player = Player("Alice", 0)

    print("Player name:", player.name)
    print("Player color:", player.color)

    move = player.askMove()
    print("Move entered:", move)

    print("Player Test OK!")
