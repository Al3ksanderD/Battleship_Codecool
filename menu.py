import time
from clint.textui import colored
import pyfiglet
import sys

def welcom():
  welcom = pyfiglet.figlet_format("WELCOM IN BATTLESHIP !", font = "slant")
  print(colored.red(welcom))
  time.sleep(1)

welcom()

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

menu()

option = int(input("Please choose from presented options: "))

def goodbye():
  goodbye = pyfiglet.figlet_format("GOODBYE !", font = "slant")
  print(colored.red(goodbye))
  sys.exit()
        
goodbye() 


def get_player_names():
    pass

