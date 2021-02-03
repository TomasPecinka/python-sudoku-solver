import time

BOARD = [[4, 0, 0, 0, 0, 0, 0, 9, 0],
         [0, 0, 0, 6, 0, 0, 0, 1, 0],
         [1, 8, 0, 7, 0, 4, 0, 0, 0],
         [9, 0, 2, 0, 5, 0, 0, 8, 0],
         [5, 0, 0, 0, 8, 0, 0, 0, 2],
         [0, 4, 0, 0, 2, 0, 9, 0, 5],
         [0, 0, 0, 1, 0, 8, 0, 6, 9],
         [0, 6, 0, 0, 0, 3, 0, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 0, 7]]

solved_time = 0

def print_board(board):
    # print board in more user-friendly way
    for col in range(len(board)):
        if (col % 3 == 0 and col > 0):
            print("-" * 21)

        for row in range(len(board[0])):
            if (row % 3 == 0 and row > 0):
                print("|", end = " ")
            print(board[col][row], end = " ")
        print("")


def find_empty(board):
    # find blank field in board
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return [row, col]   # return list with coordinates
    return None
    
def validate_board(board, num, pos):
    # validate row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # validate column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # validate sub-square
    x_square = pos[1] // 3
    y_square = pos[0] // 3

    for i in range(y_square * 3, (y_square * 3) + 3):
        for j in range(x_square * 3, (x_square * 3) + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True    

def solve_board(board):
    # check if the board has blank field
    empty = find_empty(board)
    if not empty:                   # if no blank field is find, the board is solved                                  
        return True                                  
    else:
        row, col = empty            # if blank field exists, function continues

    for i in range(1, 10):                           # generate numbers from 1 to 9
        if validate_board(board, i, (row, col)):     # validate the board with newly generated number
            board[row][col] = i                         # if the number fits, it is added to the board

            if solve_board(board):                      # recursively call function solve_board() again with updated parameter
                return True                             

            board[row][col] = 0                         # if the board cannot be solved, reset last number

    return False                                        # and try again with new number


print("___ SUDOKU SOLVER ___")
print("\n_______ BOARD _______\n")

print_board(BOARD)
start_time = time.time()
solve_board(BOARD)
solved_time = time.time() - start_time
print("\n______ SOLVED _______\n")
print_board(BOARD)
print("\nsolved in {:.5f} sec.".format(solved_time))