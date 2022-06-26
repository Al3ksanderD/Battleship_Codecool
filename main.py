# Constant values
HEIGHT = 10  # Póki co ustawiłem jak stałe wartości ale jak dorobię funkcję do zmiany rozmiaru
WIDTH = 10  # planszy to to zmienię
BLUE = (57, 197, 243)
RED = (255,37,88)


# Functions
def colored(rgb, text):  # RGB Colors function
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def place_ships(size, startingXY, secondXY, position):
    """

    Size - length of the ship
    StartingXY - the starting coordinate of the ship
    SecondXY - the coordinate of the adjacent ship tile
    Position - Horizontal or Vertical
    """


def draw_grid(width, height, turn):
    """
    W - Water
    S - Ship
    M - Missed Shot
    T - Target Hit
    """
    alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'K',
                13: 'M', 14: 'N',
                15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
                26: 'Z'
                }
    global water, grid_friendly, grid_enemy
    water = colored(BLUE, 'W')
    grid_friendly = [[water] * width for i in range(height)]
    grid_enemy = [[water] * width for i in range(height)]


    if turn == 1:
        grid = grid_friendly
    else:
        grid = grid_enemy
    counter = 1
    print("     ", end="")
    for x in range(width):
        colored_value = colored(RED, x)
        print(f"{colored_value}", end="  ")
    print("")
    for x in grid:
        colored_value = colored(RED, alphabet[counter])
        print(colored_value, end =" |")
        counter += 1
        for y in x:
                print(f" {y}", end="|")
        print("")
        print("   ",end="")
        for y in x:
            print("|---", end="")

        print("|")




print(BLUE[0])
draw_grid(WIDTH, HEIGHT, 1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
