
# Constant values
HEIGHT = 10  # Póki co ustawiłem jak stałe wartości ale jak dorobię funkcję do zmiany rozmiaru
WIDTH = 10   # planszy to to zmienię
BLUE = (57,197,243)

# Functions
def colored(rgb, text): # RGB Colors function
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def draw_grid(width, height):
    """
    W - Water
    S - Ship
    M - Missed Shot
    T - Target Hit
    """
    water = colored(BLUE, 'W')
    grid = [[water] * width for i in range(height)]
    for x in grid:
        for y in x:
            print(y, end=" ")

        print("\n")


print(BLUE[0])
draw_grid(WIDTH, HEIGHT)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
