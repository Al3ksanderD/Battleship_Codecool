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


def convert_human_readable_coordinates_to_index_based(human_readable_coordinates: tuple):
    row_letter_to_index = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
        'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
        'Z': 25
    }
    index_based_coordinates: tuple = (None, None)
    index_based_coordinates[0] = row_letter_to_index[human_readable_coordinates[0]]
    index_based_coordinates[1] = human_readable_coordinates[1] - 1


def convert_index_based_coordinates_to_human_readable(index_based_coordinates: tuple):
    row_index_to_letter = {
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
        13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
        25: 'Z'
    }
    human_readable_coordinates: tuple = (None, None)
    human_readable_coordinates[0] = row_index_to_letter[index_based_coordinates[0]]
    human_readable_coordinates[1] = index_based_coordinates[1] + 1

