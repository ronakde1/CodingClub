# Hard

# Function to check if a given number 'num' can be placed at 'row' and 'col' in the Sudoku board
def is_valid(board, row, col, num):
    # Check if 'num' is not already in the current row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is not already in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# Recursive function to solve the Sudoku puzzle
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Try placing 'num' in the empty cell
                        if solve_sudoku(board):  # Recursively try to solve the board
                            return True
                        board[row][col] = 0  # Backtrack if no valid solution found
                return False  # No valid number can be placed here, backtrack

    return True  # All cells filled, the puzzle is solved


# Example Sudoku puzzle (0 represents empty cells cuz y not)
sudoku_board_example = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Attempt to solve the Sudoku puzzle
if solve_sudoku(sudoku_board_example):
    for row in sudoku_board_example:
        print(row)  # Print the solved Sudoku board cuz
else:
    print("No solution exists for this Sudoku puzzle.")
