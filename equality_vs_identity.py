



class Piece:
    def __init__(self, piece_type):
        self.x = 0
        self.y = 0
        self.piece_type = piece_type

    def __eq__(self, other):
        return self.piece_type == other.piece_type and self.x == other.x and self.y == other.y


pawn1 = Piece('pawn')
pawn2 = Piece('pawn')

last_moved_piece = pawn1



print("Pawns are equal? {}".format(pawn1 == pawn2))
print("Pawns are identical? {}".format(pawn1 is pawn2))

print("Last moved piece identical to pawn1? {}".format(pawn1 is last_moved_piece))


