def square_matrix(matrix):
    squared_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return squared_matrix
