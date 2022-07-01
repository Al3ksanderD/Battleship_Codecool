def determine_ship_lengths(board_size):
    ship_lengths = []
    number_of_ship_fields = 0.2 * board_size * board_size
    ship_length = 0
    sum_of_lengths = 0
    while sum_of_lengths <= number_of_ship_fields:
        ship_length += 1
        ship_lengths.append(ship_length)
        sum_of_lengths += ship_length
    return ship_lengths


def get_ships_placement(ship_lengths: list, player, game_mode):
    print(player, ", please, place your ships on the board.")
    row_letter_to_index = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }
    for ship_length in ship_lengths:
        if ship_length == 1:
            print("Choose where to place a ship of length 1 (coordinates in form letter+number, e.g. A1): ")
        else:
            print("Choose where to place a ship of length", ship_length, "(coordinates in form letter+number, e.g. A1): "
                                                                         "")


def get_shot_coordinates(boards, player, game_mode):
    print(player, ", please, give a shot: ")
    row_letter_to_index = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }
