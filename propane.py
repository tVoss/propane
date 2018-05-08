#!/usr/bin/python

import random

def main():
    board = generate_soduko(50)
    print_soduko(board)

def verify_soduko(board):

    print 'Verifying rows...'

    columns = [[]] * 9
    for row in board:
        # Quick check first
        if len(row) != len(set(row)):
            return False
    
        for i, box in enumerate(row):
            # Build out the columns
            columns[i].append(box)

    print 'Verifying coulmns...'

    # Now the columns
    for column in columns:
        if len(column) != len(set(column)):
            return False

    print 'Verifying boxes...'

    # Gettin tricky
    grids = [None] * 9
    for i in range(3):
        for j in range(3):
            grids[i * 3 + j] = [
                board[i * 3][j * 3], 
                board[i * 3 + 1][j * 3], 
                board[i * 3 + 2][j * 3],
                
                board[i * 3][j * 3 + 1], 
                board[i * 3 + 1][j * 3 + 1], 
                board[i * 3 + 2][j * 3 + 1],
                
                board[i * 3][j * 3 + 2], 
                board[i * 3 + 1][j * 3 + 2], 
                board[i * 3 + 2][j * 3 + 2],
            ]
    for grid in grids:
        if (len(grid)) != len(set(grid)):
            return False

    return True

def generate_soduko(num_boxes):
    board = []
    for j in range(9):
        board.append([])
        for _ in range(9):
            board[j].append(0)

    for _ in range(num_boxes):
        place_box(board)
    return board

def place_box(board):
    open_spots = []
    for j, row in enumerate(board):
        for i, box in enumerate(row):
            if box == 0:
                open_spots.append((i, j))

    (x, y) = random.choice(open_spots)
    canidates = get_canidates(board, x, y)
    while len(canidates) == 0:
        open_spots.remove((x, y))
        # You're in trouble now
        if len(open_spots) == 0:
            return
        (x, y) = random.choice(open_spots)

    board[y][x] = random.choice(canidates)
    
def get_canidates(board, x, y):
    values = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Clear out the row
    for box in enumerate(board[y]):
        values.discard(box)

    # Clear the column
    for j in range(len(board)):
        values.discard(board[j][x])

    # Getting weird again
    i = x % 3
    j = y % 3

    values.discard(board[j][i])
    values.discard(board[j][i + 1])
    values.discard(board[j][i + 2])
    values.discard(board[j + 1][i])
    values.discard(board[j + 1][i + 1])
    values.discard(board[j + 1][i + 2])
    values.discard(board[j + 2][i])
    values.discard(board[j + 2][i + 1])
    values.discard(board[j + 2][i + 2])

    return list(values)

def print_soduko(board):
    string = ''

    for j, row in enumerate(board):
        for i, box in enumerate(row):
            string += str(box) + ' '

            if (i == len(row) - 1):
                string += '\n'
            elif (i + 1) % 3 == 0:
                string += '| '


        if (j + 1) % 3 == 0 and not j == len(row) - 1:
            string += '------+-------+------\n'
    
    print string

if __name__ == '__main__':
    main()