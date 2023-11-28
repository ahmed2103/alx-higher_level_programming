#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def init_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def chessboard_deepcopy(chessboard):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in chessboard]

def get_queen_positions(chessboard):
    """Return the list of lists representation of a chessboard with queens."""
    positions = []
    for row, row_values in enumerate(chessboard):
        for col, cell in enumerate(row_values):
            if cell == 'Q':
                positions.append([row, col])
    return positions

def mark_attacked_positions(chessboard, row, col):
    """Mark attacked positions on a chessboard."""
    n = len(chessboard)
    for i in range(n):
        chessboard[row][i] = chessboard[i][col] = 'x'
    for i in range(1, n):
        if row + i < n and col + i < n:
            chessboard[row + i][col + i] = 'x'
        if row - i >= 0 and col - i >= 0:
            chessboard[row - i][col - i] = 'x'
        if row + i < n and col - i >= 0:
            chessboard[row + i][col - i] = 'x'
        if row - i >= 0 and col + i < n:
            chessboard[row - i][col + i] = 'x'

def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    
    Returns:
        solutions
    """
    n = len(chessboard)
    if queens == n:
        solutions.append(get_queen_positions(chessboard))
        return solutions

    for col in range(n):
        if chessboard[row][col] == ' ':
            tmp_chessboard = chessboard_deepcopy(chessboard)
            tmp_chessboard[row][col] = 'Q'
            mark_attacked_positions(tmp_chessboard, row, col)
            solutions = recursive_solve(tmp_chessboard, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = init_chessboard(N)
    solutions = recursive_solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
