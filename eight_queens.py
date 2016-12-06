import os
from time import sleep

if os.name == 'nt':
    clear_screen = 'cls'
elif os.name == 'posix':
    clear_screen = 'clear'

def print_chess_board(chess_board):
    sleep(0.1)
    os.system(clear_screen)
    for row in chess_board:
        print '|'.join(row)

def eight_queens(col, chess_board):
    print_chess_board(chess_board)
    if col == 8:
        raw_input('Solution found. Press enter to quit.')
        return True
    for row in range(0,8):
        if not conflict(row, col, chess_board):
            chess_board[row][col] = ' Q '
            if eight_queens(col + 1, chess_board):
                return True
        chess_board[row][col] = '   '
    return False

def conflict(row, col, chess_board):
    if( exists_in_row(row, chess_board)                     or
        exists_in_downward_diagonal(row, col, chess_board)  or
        exists_in_upward_diagonal(row, col, chess_board)):
        return True
    return False

def exists_in_row(row, chess_board):
    return ' Q ' in chess_board[row]

def exists_in_downward_diagonal(row, col, chess_board):
    if out_of_bounds(row,col):
        return False
    else:
        if chess_board[row][col] == ' Q ':
            return True
        else:
            return exists_in_downward_diagonal(row - 1, col - 1, chess_board)

def exists_in_upward_diagonal(row, col, chess_board):
    if out_of_bounds(row,col):
        return False
    else:
        if chess_board[row][col] == ' Q ':
            return True
        else:
            return exists_in_downward_diagonal(row + 1, col - 1, chess_board)

def out_of_bounds(row,col):
    return row < 0 or col < 0 or row > 7 or col > 7

def get_empty_chess_board():
    return [['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   '],
            ['   ','   ','   ','   ','   ','   ','   ','   ']]

def solve_eight_queens():
    eight_queens(0, get_empty_chess_board())

solve_eight_queens()
