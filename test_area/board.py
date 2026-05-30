
import json
from typing import Optional, List, Type, Dict
from test_position_class import Position
from pieces.base import Piece
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.pawn import Pawn

class Board:
    def __init__(self):
        self._grid: List[List[Optional[Piece]]] = [[None]*8 for _ in range(8)]
        self._pieces: List[Piece] = []
        self.init()

    def init(self):
        self._grid = [[None]*8 for _ in range(8)]
        self._pieces = []

        def place(p: Piece):
            r, c = p.position.to_tuple()
            self._grid[r][c] = p
            self._pieces.append(p)

        # White
        place(Rook(Position('a',1),0)); place(Knight(Position('b',1),0)); place(Bishop(Position('c',1),0))
        place(Queen(Position('d',1),0)); place(King(Position('e',1),0))
        place(Bishop(Position('f',1),0)); place(Knight(Position('g',1),0)); place(Rook(Position('h',1),0))
        for col in "abcdefgh": place(Pawn(Position(col,2),0))
        # Black
        place(Rook(Position('a',8),1)); place(Knight(Position('b',8),1)); place(Bishop(Position('c',8),1))
        place(Queen(Position('d',8),1)); place(King(Position('e',8),1))
        place(Bishop(Position('f',8),1)); place(Knight(Position('g',8),1)); place(Rook(Position('h',8),1))
        for col in "abcdefgh": place(Pawn(Position(col,7),1))

    def getPosition(self, piece: Piece):
        return piece.position if piece in self._pieces else None

    def getPiece(self, position: Position) -> Optional[Piece]:
        r, c = position.to_tuple()
        return self._grid[r][c]

    def movePiece(self, piece: Piece, dest: Position):
        orow, ocol = piece.position.to_tuple()
        drow, dcol = dest.to_tuple()
        captured = self._grid[drow][dcol]
        if captured and captured in self._pieces:
            self._pieces.remove(captured)
        self._grid[orow][ocol] = None
        self._grid[drow][dcol] = piece
        piece.position = dest

    def all_pieces(self) -> List[Piece]:
        return list(self._pieces)

    def serialize(self) -> Dict:
        data = []
        for p in self._pieces:
            data.append({
                "type": p.__class__.__name__,
                "color": p.color,
                "pos": {"col": p.position.column, "row": p.position.row}
            })
        return {"pieces": data}

    @staticmethod
    def deserialize(data: Dict) -> "Board":
        type_map: Dict[str, Type[Piece]] = {
            "King": King, "Queen": Queen, "Bishop": Bishop, "Knight": Knight, "Rook": Rook, "Pawn": Pawn
        }
        b = Board()
        b._grid = [[None]*8 for _ in range(8)]
        b._pieces = []
        for item in data["pieces"]:
            cls = type_map[item["type"]]
            color = int(item["color"])
            pos = Position(item["pos"]["col"], int(item["pos"]["row"]))
            p = cls(pos, color)  # type: ignore
            r, c = pos.to_tuple()
            b._grid[r][c] = p
            b._pieces.append(p)
        return b

    # test helpers (optional but useful)

