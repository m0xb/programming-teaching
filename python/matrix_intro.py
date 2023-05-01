
def matrix_multiply(A, B):
    # check to see if the multiplication is legal
    # Number of cols in first must equal number of rows in second
    a_cols = len(A[0])
    b_rows = len(B)
    if a_cols == b_rows:
        # do multiplication
        result_matrix = []
        # pre-fill the result with the same number of rows as A
        a_rows = len(A)

        # Currently: Add an 1-item list for each row in the result matrix
        # BUT, we want this to be "flexible" and work with any number of b_cols
        # so: we actually want to add extra values in each sub-list
        # so, restate: Add an N-item list for each row in the result matrix where N=b_cols
        for current_row in range(a_rows):
            result_matrix.append([0]*len(B[0]))
            # for _ in range(len(B[0]) - 1):
            #     result_matrix[current_row].append(0)

        for b_col in range(len(B[0])):
            for b_idx, b_row in enumerate(B):
                for a_idx, a_row in enumerate(A):
                    val = b_row[b_col] * a_row[b_idx]
                    result_matrix[a_idx][b_col] += val
        return result_matrix
    else:
        raise Exception("Cannot multiply")


A = [
    [1, 2],
    [3, 4],
    [5, 6],
]
B = [
    [2],
    [4],
]
B = [
    [2, 3],
    [4, 5],
]
B = [
    [2, 3, 4, 5],
    [4, 5, 6, 7],
]
#(3x3) x (2x3) # not valid
#(3x2) x (2x2) # valid
result = matrix_multiply(A, B)
for row in result:
    print("   ".join(map(str,row)))

