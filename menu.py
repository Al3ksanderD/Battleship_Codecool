import time
from clint.textui import colored
import pyfiglet
import sys


def welcome():
    welcome_caption = pyfiglet.figlet_format("WELCOME IN BATTLESHIP !", font="slant")
    print(colored.red(welcome))
    time.sleep(1)


def menu():
    print("****** MAIN MENU ******\n")
    time.sleep(1)
    print("1. HUMAN VS HUMAN")
    time.sleep(1)
    print("2. HUMAN VS RANDOM AI")
    time.sleep(1)
    print("3. RANDOM AI VS RANDOM AI")
    time.sleep(1)
    print("4. EXIT\n")
    time.sleep(1)


# option = int(input("Please choose from presented options: "))


def goodbye():
    goodbye_caption = pyfiglet.figlet_format("GOODBYE !", font="slant")
    print(colored.red(goodbye))
    sys.exit()


def get_player_names():
    pass
