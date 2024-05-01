import sys

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, N):
                return True
            board[i][col] = 0

    return False

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        return []

    solutions = []
    for row in board:
        solution = []
        for i, col in enumerate(row):
            if col == 1:
                solution.append([i, row.index(col)])
        solutions.append(solution)

    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be a number and >= 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)

