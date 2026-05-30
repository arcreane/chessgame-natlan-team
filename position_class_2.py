from dataclasses import dataclass
# dataclass is a decorator that examines the class to find fields
@dataclass(frozen=True) # frozen=True means the class' values cant be changed after creation
class Position:
    column: str  # 'a'..'h'
    row: int     # 1..8

# @dataclass adds this automatically:
#    def __init__(self, col, row):
#       self.column = col
#       self.row = row

    def __post_init__(self): # special dataclass method that automatically runs after __init__
        print("post")
        if self.column not in "abcdefgh":
            raise ValueError(f"Invalid column: {self.column}")
        if not (1 <= self.row <= 8):
            raise ValueError(f"Invalid row: {self.row}")
    # checks that the column and row are in the possible values

# convert a chess position with a letter and number into grid coordinates
    def to_tuple(self): 
        # 0-based internal grid (row, col)
        c = ord(self.column) - ord('a')
        r = 8 - self.row
        return (r, c)

    @staticmethod
    def from_tuple(rc):
        r, c = rc
        return Position(chr(ord('a') + c), 8 - r)

    def __str__(self):
        return f"{self.column}{self.row}"

test = Position("js",3)
print({test})