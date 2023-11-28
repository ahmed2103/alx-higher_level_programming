#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an N×N chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

The program should print every possible solution to the problem.
One solution per line.

Format: see example
You don’t have to print the solutions in a specific order.

You are only allowed to import the sys module.

Read: Queen, Backtracking
"""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == 'Q':
                solution.append([r, c])
    return solution

def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    n = len(board)
    for i in range(n):
        board[row][i] = board[i][col] = 'x'
    for i in range(1, n):
        if row + i < n and col + i < n:
            board[row + i][col + i] = 'x'
        if row - i >= 0 and col - i >= 0:
            board[row - i][col - i] = 'x'
        if row + i < n and col - i >= 0:
            board[row + i][col - i] = 'x'
        if row - i >= 0 and col + i < n:
            board[row - i][col + i] = 'x'

def recursive_solve(board, row, queens):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.

    Returns:
        solutions
    """
    n = len(board)
    if queens == n:
        print_solution(board)
        return

    for c in range(n):
        if board[row][c] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = 'Q'
            xout(tmp_board, row, c)
            recursive_solve(tmp_board, row + 1, queens + 1)

def print_solution(board):
    """Print the solution in the specified format."""
    solution = get_solution(board)
    print(solution)

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

    board = init_board(N)
    recursive_solve(board, 0, 0)
