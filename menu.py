import time
from clint.textui import colored
import pyfiglet
# import sys


def welcome():
    welcome_caption = pyfiglet.figlet_format("WELCOME IN BATTLESHIP !", font="slant")
    print(colored.red(welcome_caption))
    time.sleep(1)


def display_instructions():
    pass


def exit_game():
    raise SystemExit


def get_game_mode():
    """
        Should print a menu with the following options:
        1. Human vs Human
        2. Human vs AI
        3. AI vs AI

        The function should return a number between 1-3.
        If the user will enter invalid data (for example 5), than a message will appear
        asking to input a new value.
        The function prints the instructions of a game if option 4 is chosen. Then calls itself and asks user to choose
        game mode unless user chooses to end the game typing quit, exit or close.
        """

    print("""
    Game modes:
        1. Human vs Human
        2. Human vs AI
        3. AI vs AI
    Instructions:
        4. Display legend
            """)
    while True:
        player_input = input("Choose a game mode typing an option from one to three: ")
        if player_input == "quit" or player_input == "exit" or player_input == "close":
            print("Bye bye!")
            exit_game()
        else:
            try:
                game_mode = int(player_input)
            except ValueError:
                print("Please enter a number! Choose from 1-4: ")
                continue
            if game_mode < 1 or game_mode > 4:
                print("Wrong choice. Please choose option between 1-4")
                continue
            if game_mode == 4:
                display_instructions()
                get_game_mode()
            else:
                return game_mode


def goodbye():
    goodbye_caption = pyfiglet.figlet_format("GOODBYE !", font="slant")
    print(colored.red(goodbye_caption))
    exit_game()


def get_player_names(game_mode):
    human_vs_human = 1
    human_vs_ai = 2
    ai_vs_ai = 3
    if game_mode == human_vs_human or game_mode == human_vs_ai:
        ai_names = ["Hermes", "Pilot", "Pan Tadeusz", "Shooting Duck", "Houston", "Afrodyta", "Kira", "Dr. Strange",
                    "Jełgeniusz Majewski", "Jegomość Skroniawski", "Miss Burza", "Oragon", "Pretensyja", "Zhang",
                    "Joanna Jędrzejczyk", "Minor", "Per Haps", "Kierownik masztu", "Piekielna Matylka", "Hitchhiker"]
    players = []
    second_name_entered = False
    second_player_name = False
    if game_mode == human_vs_human:
        players.append(input("First player, please enter your name: "))
        while not second_name_entered:
            second_player_name = input("Second player, please enter your name: ")
            if second_player_name is False or second_player_name == "":
                continue
            second_name_entered = validate_different_player_names([players[0], second_player_name])
            if second_name_entered:
                print("Thank you.")
            else:
                print("It seems as though names of two players are same. Please try again.")
        players.append(second_player_name)
    elif game_mode == human_vs_ai:
        from random import choice
        players.append(input("Please enter your name: "))
        while not second_name_entered:
            second_player_name = choice(ai_names)
            if second_player_name is False or second_player_name == "":
                continue
            second_name_entered = validate_different_player_names([players[0], second_player_name])
            if second_name_entered:
                print("Thank you.")
        players.append(second_player_name)
    elif game_mode == ai_vs_ai:
        from random import sample
        players = sample(ai_names, 2)
    return players


def validate_different_player_names(players):
    """Takes in an arbitrary length array of strings and compare them for differences.
    If names are different return True, else return False"""
    for current_player_index, player in enumerate(players):
        for player_index in range(current_player_index + 1, len(players)):
            if current_player_index != player_index:
                if player == players[player_index]:
                    return False
    return True


def get_board_size(board_size_limit):
    if not board_size_limit:
        board_size_limit = (5, 10)
    while True:
        try:
            board_size = int(input("Choose board size between", board_size_limit[0], "and", board_size_limit[1], ": "))
            if board_size_limit[0] <= board_size <= board_size_limit[1]:
                return board_size
            else:
                print("Invalid input. Board size out of range.")
        except ValueError:
            print("Please enter a number.")
