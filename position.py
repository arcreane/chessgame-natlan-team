class Position:
        def __init__(self, column, row):
            self.column = column
            self.row = row

        def __str__(self):
            return f"{self.column}{self.row}"


class Test:
    def __init__(self, column, row):
            self.column = column
            self.row = row


if __name__ == "__main__":
    p1 = Position("e", 4)
    print(f"Position created: {p1}")

    p2 = Position("a", 1)
    print(f"Position created: {p2}")

    p3 = Test("b", 2)
    print(f"Position created: {p3}")
    print("Tests Position OK!")
