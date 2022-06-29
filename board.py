def initialise_empty_board(player, dimensions=10):
    board = {player: []}
    for row in range(dimensions):
        board[player].append([])
        for column in range(dimensions):
            board[player][row].append(0)
    return board


def display_boards(boards: dict, player_names, board_dimensions=False):
    column_letters = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
        14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
        26: 'Z'
    }
    for player in player_names:
        if player in boards:
            print(player)
            if not board_dimensions:
                board_dimensions = len(boards[player][0])

            for column_index in range(board_dimensions):
                print(column_letters[column_index+1], " ", end="")

            for row_number, row in enumerate(boards[player]):
                print(row_number, " |", end="")
                for item in row:
                    if item == 0:
                        print("~", end="")  # Water
                    elif item == 1:
                        print("X", end="")  # Hit
                    elif item == 2:
                        print("·", end="")  # Miss
                    elif item == 3:
                        print("S", end="")  # Sunk
                    print("|")
                print()
