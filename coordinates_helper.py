from constants import *
from random import choice
from menu import exit_game


def is_player_valid(boards, player):
    if player in boards:
        return True
    else:
        return False

def is_player_ai(boards, player):
    try:
        if player in boards and player == boards[1]:
            return True
        elif player in boards and player == boards[0]:
            return False
        else:
            raise KeyError("Player was not found in boards...")
    except KeyError:
        print(KeyError)

def determine_ship_lengths(board_size):
    ship_lengths = []
    number_of_ship_fields = 0.2 * board_size * board_size
    ship_length = 1
    sum_of_lengths = 0
    while sum_of_lengths <= number_of_ship_fields:
        ship_length += 1
        ship_lengths.append(ship_length)
        sum_of_lengths += ship_length
    return ship_lengths


def convert_human_readable_coordinate_to_index_based(human_readable_coordinates):
    index_based_coordinates = [None, None]
    index_based_coordinates[0] = row_letter_to_index[human_readable_coordinates[0]]
    index_based_coordinates[1] = human_readable_coordinates[1] - 1
    return index_based_coordinates


def convert_index_based_coordinate_to_human_readable(index_based_coordinates):
    human_readable_coordinates = [None, None]
    human_readable_coordinates[0] = row_index_to_letter[index_based_coordinates[0]]
    human_readable_coordinates[1] = index_based_coordinates[1] + 1
    return human_readable_coordinates


def is_coordinate_on_board(coordinate, board_dimension):
    min_index = 0
    max_index = board_dimension - 1
    for index in coordinate:
        if index < min_index or index > max_index:
            return False
    return True


def is_player_coordinate_valid(boards, player_coordinate, board_dimension=None):
    board_dimension_is_valid(board_dimension, boards)
    board_dimension = get_all_boards_dimension(board_dimension, boards)

    if len(player_coordinate) == 2:
        expected_row_letter = player_coordinate[0]
        expected_column_number = player_coordinate[1]
        if len(expected_row_letter) == 1 and expected_row_letter.isalpha():
            if len(expected_column_number) == 1 and expected_column_number.isnumeric():
                try:
                    expected_column_number = int(expected_column_number)
                except ValueError:
                    return False
                index_based_coordinate = convert_human_readable_coordinate_to_index_based((expected_row_letter,
                                                                                            expected_column_number))
                if is_coordinate_on_board(index_based_coordinate, board_dimension):
                    return True
    else:
        return False


def get_all_boards_dimension(boards):
    try:
        if (len(boards[0]["ship placement"]) == len(boards[1]["ship placement"]) == len(boards[0]["shooting"]) ==
            len(boards[1]["shooting"])):
            return len(boards[0]["ship placement"])
        else:
            raise ValueError("Problem determining the size of the board: boards are of different dimensions.")
    except ValueError:
        print(ValueError)
        exit_game()


def board_dimension_is_valid(board_dimension, boards):
    if board_dimension == get_all_boards_dimension(boards):
        return True
    else:
        return False


def get_possible_ship_placements(boards, player):
    free_water_coordinates = []
    board = boards[player]["ship placement"]
    for row_index, row in enumerate(board):
        for column_index, field in enumerate(row):
            if field == 0:
                free_water_coordinates.append((row_index, column_index))
    return free_water_coordinates


def get_own_coordinate_from_human(boards, player, ship_size: int):
    print("For ship of size", ship_size, end='')
    player_coordinate = input(". Please enter your start and end coordinates separated by a comma:")
    two_coordinates = player_coordinate.strip().split()
    for coordinate in two_coordinates:
        coordinate.strip()
        coordinate_is_validated = is_player_coordinate_valid(boards, coordinate)
    if coordinate_is_validated:
        index_based_coordinates = convert_human_readable_coordinate_to_index_based(coordinate)
        return index_based_coordinates
    elif not coordinate_is_validated:
        print("The coordinate was not valid. Please try again: ")
        return get_own_coordinate_from_human(boards, player, ship_size)
    # TODO
    # convert to index form
    # check if on board, check if free

def get_own_coordinate_from_ai(boards, player, ship_length):
    players_board = boards[player]["ship placement"]
    possible_placements = get_possible_ship_placements(players_board)
    boards[player]["ship placement"]
    coordinate = choice(possible_placements)
    # AI tales direction either SOUTH or EAST

    return coordinate, direction

def add_own_coordinate_to_board


def get_shot_coordinate_from_human(boards, player):
    for board_player in boards:
        if board_player ==
    # boards[player]

def get_shot_coordinate_from_ai(boards, player):
    boards[player]


def is_ai_coordinate_valid(boards, ai_coordinate, board_dimension):
    pass
