def create_matrix(n, a1, a2, a3):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = a1
            elif i == j + 1 or i == j - 1:
                matrix[i][j] = a2
            elif i == j + 2 or i == j - 2:
                matrix[i][j] = a3
    return matrix


def copy_matrix(matrix):
    copy = []
    for row in matrix:
        copied_row = []
        for value in row:
            copied_row.append(value)
        copy.append(copied_row)
    return copy


def create_diagonal_matrix(vector):
    n = len(vector)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = vector[i]
    return matrix
