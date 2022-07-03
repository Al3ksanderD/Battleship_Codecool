from board import *
from menu import *
from tests import *
from playsound import playsound
from coordinates import *
from constants import *

# Constant values

# Functions


def game_flow(game_mode=False, board_size_limit=False):
    # TODO game mode validation
    game_running = True
    try:
        if not game_mode:
            game_mode = get_game_mode()
        board_size = get_board_size(board_size_limit)
        boards = initialise_empty_boards(get_player_names(game_mode), board_size)
        phase = "ship placement"
        for player in boards.keys():
            display_board(boards, player, phase, board_size)
            get_ships_placement(determine_ship_lengths(board_size), player, game_mode)
        phase = "shooting"
        while game_running:
            for player in boards.keys():
                display_board(boards, player, phase, board_size)
                get_shot_coordinates(boards, player, game_mode)
    # TODO : check below
    # except ValueError:
    #     print(ValueError)
    #     try:
    #         decision = input("Would you like to try again choosing a board size within the limit range? y/n")
    #         if decision.lowercase() == "y" or decision.lowercase() == "yes":
    #             game_flow(game_mode, (5, 10))
    #         elif decision.lowercase() == "n" or decision.lowercase() == "no":
    #             goodbye()
    #     except SystemExit:
    #         print()
    except SystemExit:
        print()


def colored(rgb, text):  # RGB Colors function
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def ai_ship_generator():
    pass


def shoot_ship(grid, input_xy, points):
    """
    grid: The grid that we pass, friendly or enemy
    input_xy: The cords of the intended shot
    points: if hit we add point to the player that made the shot
    """
    cord_x = input_xy[0]
    cord_y = input_xy[1] - 1
    target_hit = colored(RED, "T")
    missed_shot = colored(GREY, "M")
    check_grid = (grid[cord_y][cord_x] == "\x1b[38;2;71;192;70mS \x1b[38;2;255;255;255m")
    if check_grid:
        grid[cord_y][cord_x] = target_hit
        points += 1
        return points
    else:
        grid[cord_y][cord_x] = missed_shot
        

def place_ships(size, startingXY, lastXY, position, player):
    """

    Size - length of the ship
    StartingXY - the starting coordinate of the ship
    SecondXY - the coordinate of the adjacent ship tile
    Position - Horizontal or Vertical
    Player - to what player does the ships belong to
    """
    startX = startingXY[0]
    startY = startingXY[1] - 1
    lastX = lastXY[0]
    lastY = lastXY[1] - 1
    colored_value = colored(GREEN, "S")
    if player == 1:
        if position == "H":

            check_direction = startX - lastX
            if check_direction > 0:
                for cord in range(size):
                    grid_friendly[startY][startX] = colored_value
                    startX -= 1

            else:
                for cord in range(size):
                    grid_friendly[startY][startX] = colored_value
                    startX += 1
                pass
        else:
            check_direction = startY - lastY
            if check_direction > 0:
                for cord in range(size):
                    grid_friendly[startY][startX] = colored_value
                    startY -= 1

            else:
                for cord in range(size):
                    grid_friendly[startY][startX] = colored_value
                    startY += 1
                pass
    if player == 2:
        if position == "H":

            check_direction = startX - lastX
            if check_direction > 0:
                for cord in range(size):
                    grid_enemy[startY][startX] = colored_value
                    startX -= 1

            else:
                for cord in range(size):
                    grid_enemy[startY][startX] = colored_value
                    startX += 1
                pass
        else:
            check_direction = startY - lastY
            if check_direction > 0:
                for cord in range(size):
                    grid_enemy[startY][startX] = colored_value
                    startY -= 1

            else:
                for cord in range(size):
                    grid_enemy[startY][startX] = colored_value
                    startY += 1
                pass


        """
        Tą funkcję będzie trzeba trochę skrócić bo się mnóstwo
        kodu powtarza ale zajmę się tym jak już cała gra będzie działać
        """

    else:
        pass


def draw_grid(width, grid, turn):
    """
    W - Water
    S - Ship
    M - Missed Shot
    T - Target Hit
    """


    counter = 1
    print("     ", end="")
    for x in range(width):
        colored_value = colored(RED, x)
        print(f"{colored_value}", end="  ")
    print("")
    for x in grid:
        colored_value = colored(RED, alphabet[counter])
        print(colored_value, end=" |")
        counter += 1
        for y in x:
            print(f" {y}", end="|")
        print("")
        print("   ", end="")
        for y in x:
            print("|---", end="")

        print("|")


# Zmienne są tu tymczasowo jak wymyślę co z nimi zrobić przerzucę je gdzieś indziej
# water = colored(BLUE, 'W')
# grid_friendly = [[water] * WIDTH for i in range(HEIGHT)]
# grid_enemy = [[water] * WIDTH for i in range(HEIGHT)]


#draw_grid(WIDTH, grid_friendly, 1)
# place_ships(3, (3, 8), (3, 5), "V", 2)
# draw_grid(WIDTH, grid_enemy, 1)
# print(list(alphabet.keys())[list(alphabet.values()).index("A")])
# playsound(u"sounds/background.mp3")
if __name__ == '__main__':
    welcome()
    game_flow()
    # test()
