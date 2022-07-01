from collections import OrderedDict


class Ship:
    def __init__(self, length, start_field: tuple, end_field: tuple, board: list, other_ships: list):
        raise ValueError("The ship needs to be placed in straight line either ")
        self.length = length
        self.start_field = start
        self.no_other_ship_area = []

    def check_length(self, length, start_coordinate, end_coordinate):
        pass

    direction: int = 3
    length = 1


def initialise_empty_boards(players, board_size=10):
    """Creates an empty board for each player for a Battleship game play. The boards are used to present a current
    state of a gameplay. During the gameplay, before shooting, player whose turn it is is presented with a board on
    which marked are fields to which the player has shot, with the symbols marking whether there was a Hit "X" or
    Miss "·" or if the ship was sunk "S". Fields where the player didn't shot at are unknown and are marked as ~,
    which means that at those fields there either may be a ship or there may be no ship present.
    After giving a shot player is presented with the feedback if the shot has reached any ship of the opponent.
    The updated board is presented with the place of shooting marked as one of the: Hit ('X'), Miss ('·') or Sunk ('S')


    Return: an ordered dictionary where keys are player names and the values are dictionaries storing boards for two
    phases of the game: ship placement and shooting.
    Keys: Names of players
    Values: dict: {"ship_placement": List List [List], "shooting": List [List]}"""
    board_size_limits = (5, 10)
    if board_size_limits[0] > board_size > board_size_limits[1]:
        raise ValueError("Board of such dimensions cannot be initialised. Must be in size limits.")
    boards = OrderedDict()
    for player in players:
        boards[player] = {"ship placement": [], "shooting": []}
        for row in range(board_size):
            boards[player]["ship placement"].append([])
            boards[player]["shooting"].append([])
            for column in range(board_size):
                boards[player]["ship placement"][row].append(0)
                boards[player]["shooting"][row].append(0)
    return boards


def display_board(boards: OrderedDict, player, phase, board_dimensions: int = False):
    """Arguments expected:
    boards: an ordered dictionary with names of players as keys and boards for each phase.
    phase: "ship placement" or "shooting".
    board_dimensions: int, optional"""

    row_index_to_letter = {
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
        13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
        25: 'Z'
    }
    if not board_dimensions:
        board_dimensions = len(boards[player][phase])
    if phase == "ship placement" and player in boards:
        print("  ", end="")
        for column_index in range(board_dimensions):
            print(column_index + 1, "", end="")
        print("")
        for row_number, row in enumerate(boards[player][phase]):
            print(row_index_to_letter[row_number], "", end="")
            for field in row:
                print(field, "", end="")
            print()
    elif phase == "shooting":
        # for bigger boards in the future development check for maximum length of row marks (they may be longer than 1
        # character and add a padding. In the current code there is an assumption made that the row has one letter mark
        # and one space padding after the mark, which gives the number of characters equal 2.
        board_width_in_number_of_characters = (board_dimensions * 2) + 2
        padding_length = 3
        padding = " " * padding_length
        player_name_captions = []
        for player in boards:
            if len(player) > board_width_in_number_of_characters:
                player_name_captions.append(player[:board_width_in_number_of_characters-3]+"...")
            elif len(player) < board_width_in_number_of_characters:
                difference = board_width_in_number_of_characters - len(player)
                player_name_caption = player + (" " * difference)
                player_name_captions.append(player_name_caption)
            elif len(player) == board_width_in_number_of_characters:
                player_name_captions.append(player)
        print(padding.join(player_name_captions))
        players = []
        for player_name in boards.keys():
            players.append(player_name)
        for row in range(board_dimensions):
            print(padding.join([boards[players[0]]["shooting"][row], boards[players[1]["shooting"][row]]]))

