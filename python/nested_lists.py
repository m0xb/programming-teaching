# 2D, 3D, 4D (and beyond) lists/arrays

# 1D list
pieces = ['pawn', 'king']
len(pieces)  # == 2

# 2D list (a "list of lists")
pieces = [['pawn'], ['rook', 'knight', 'bishop']]
len(pieces)  # == 2
len(pieces[0])  # == 1
len(pieces[1])  # == 3

# 3D list
nested = [[[9]]]
len(nested)  # == 1
len(nested[0])  # == 1
len(nested[0][0])  # == 1
nested[0][0][0]  # == 9


# Chess board as a 2D array/list
board = [
    ['Rook', 'Knight', 'Bishop'],
    ['Pawn', 'Pawn', 'Pawn'],
    [None, None, None],
    [None, None, None],
    [None, None, None],
    [None, None, None],
    ['Pawn', 'Pawn', 'Pawn'],
    ['Rook', 'Knight', 'Bishop'],
]
board[0][0]  # == 'Rook'
board[2][0]  # == None


# piece_index = 10 (row*8+col)
# c_array[5][7]
# c_array[5*row_len + 7]


# Chess board as a 3D array/list
board = [
    [
        ['Rook', 'Knight', 'Bishop'],
        ['Pawn', 'Pawn', 'Pawn'],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
    [
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        [None, None, None],
        ['Pawn', 'Pawn', 'Pawn'],
        ['Rook', 'Knight', 'Bishop'],
    ],
]

# Matrices

# Matrix (represented as 2D array)
identity_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
# Vector (represented as a 3-tuple)
v = (1, 2, 3)
# Vector (represented as a 2D list / matrix)
v2 = [
    [1],
    [2],
    [3],
]

# Scalar (represented as an int)
s = 5

identity_matrix * v == v

identity_matrix * s # -->
[
    [5, 0, 0, 0],
    [0, 5, 0, 0],
    [0, 0, 5, 0],
    [0, 0, 0, 1],
]

(identity_matrix * s) * v = (5*1, 5*2, 5*3)

