# N-Queen Problem using Backtracking (Column by Column)


# Function to check whether queen can be placed safely
def is_safe(board, row, col, n):

    # Check left side of current row
    for i in range(col):

        if board[row][i] == 'Q':
            # queen already present in same row

            return False


    # Check upper left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 'Q':
            # queen found in upper diagonal

            return False

        i -= 1
        # move upward

        j -= 1
        # move left


    # Check lower left diagonal
    i = row
    j = col

    while i < n and j >= 0:

        if board[i][j] == 'Q':
            # queen found in lower diagonal

            return False

        i += 1
        # move downward

        j -= 1
        # move left


    # if no queen attacks current position
    return True



# Function to solve N-Queen problem
def solve(board, col, n):

    # Base condition
    # all queens placed successfully

    if col == n:

        for row in board:

            print(" ".join(row))
            # print chess board

        return True


    # Try placing queen in every row
    for row in range(n):

        # Check whether position is safe
        if is_safe(board, row, col, n):

            board[row][col] = 'Q'
            # place queen

            # Recursive call for next column
            if solve(board, col + 1, n):

                return True


            # Backtracking step
            board[row][col] = '.'
            # remove queen if solution not found


    # no valid position found
    return False



# Main Program

# Input number of queens
n = int(input("Enter number of queens: "))


# Create empty chess board
board = [['.' for i in range(n)] for j in range(n)]

# '.' means empty space


# Start solving from column 0
if not solve(board, 0, n):

    print("No Solution")

-------------------
Why is N-Queen considered an AI problem?

N-Queen is considered an AI problem because:

It involves state space search
Multiple possible solutions exist
Intelligent decision making is required
Backtracking technique is used

Explain the working of Backtracking in N-Queen.

Steps:

Place queen in safe position
Move to next column
If no safe position exists:
Remove previous queen
Try another position

This process continues until solution is found.

time complexity of N-Queen Problem:O(N!)
because many queen arrangements are explored.

space complexity of N-Queen Problem:Space complexity is: O(N^2)
for storing chessboard.

What are real-life applications of backtracking?
Applications:

Sudoku solver
Maze solving
Password generation
Scheduling systems
