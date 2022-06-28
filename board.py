def initialise_empty_board(dimensions):
    board = []
    for row in range(dimensions):
        for column in range(dimensions):
            board[row][column] = 0
    return board
