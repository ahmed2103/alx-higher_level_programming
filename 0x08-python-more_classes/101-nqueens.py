#!/usr/bin/python3
import sys

def is_valid(chessboard, row, col, N):
    for i in range(row):
        if chessboard[i] == col or \
           chessboard[i] - i == col - row or \
           chessboard[i] + i == col + row:
            return False
    return True

def print_solution(chessboard):
    print([[i, chessboard[i]] for i in range(len(chessboard))])

def solve_nqueens(chessboard, row, N):
    if row == N:
        print_solution(chessboard)
        return
    for col in range(N):
        if is_valid(chessboard, row, col, N):
            chessboard[row] = col
            solve_nqueens(chessboard, row + 1, N)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = [-1] * N
    solve_nqueens(chessboard, 0, N)

if __name__ == "__main__":
    main()
