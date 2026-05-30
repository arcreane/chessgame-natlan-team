# position.py
class Position:
 def __init__(self, column, row):
    self.column = column
    self.row = row
 def __str__(self):
    return f"{self.column}{self.row}"
if __name__ == "__main__":
 # Functional tests of the Position class
    p1 = Position("e", 4)
    print(f"Position created: {p1}") # Expected: e4

    p2 = Position("a", 1)
    print(f"Position created: {p2}") # Expected: a1

print("Tests Position OK!")