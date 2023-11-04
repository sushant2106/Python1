from enum import  Enum


class Piece(Enum):
    king=1
    Queen=2
    Rook=4
    Bishop=4


class Piecvalue(Enum):
    KING=0
    Queen=34



piece=Piecvalue.Queen
print(piece.value)
