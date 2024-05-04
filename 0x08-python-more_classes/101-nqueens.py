#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the
    given position (row, col) on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen at the
        given position, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursively solve the N queens problem using backtracking.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row being considered.
        n (int): The size of the chessboard.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if row == n:
        # All queens have been successfully placed
        print([[i, board[i]] for i in range(n)])  # Print the solution
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            # If it's safe to place a queen, mark the
            # cell as occupied and recursively check the next row
            board[row] = col
            found_solution = solve_nqueens(board, row + 1, n) or found_solution
            board[row] = -1  # Backtrack

    return found_solution


def nqueens(n):
    """
    Solve the N queens problem for a given board size.

    Args:
        n (int): The size of the chessboard.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard as a list
    board = [-1] * n

    # Start solving the N queens problem
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])  # Get the board size from command line argument
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)  # Solve the N queens problem
