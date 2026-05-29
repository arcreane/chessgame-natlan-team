from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    column: str  # 'a'..'h'
    row: int     # 1..8

    def post_init(self):
        if self.column not in "abcdefgh":
            raise ValueError(f"Invalid column: {self.column}")
        if not (1 <= self.row <= 8):
            raise ValueError(f"Invalid row: {self.row}")

    def to_tuple(self):
        # 0-based internal grid (row, col)
        c = ord(self.column) - ord('a')
        r = 8 - self.row
        return (r, c)

    @staticmethod
    def from_tuple(rc):
        r, c = rc
        return Position(chr(ord('a') + c), 8 - r)

    def str(self):
        return f"{self.column}{self.row}"