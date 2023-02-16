import classes
import time
from classes import Coord

# play = classes.Player('cody')
# sc = classes.Board()
# en = classes.Board()
# classes.Board.striker(sc,en,3,1)

"""
Making a game of Battleship
"""
classes.clear_screen()
exit = False
print("Welcome to Battleship")
start = input("Enter to begin ")
while not exit:
    classes.clear_screen()
    print("Battleship")
    print()
    """
    choices to start
    """
    print('1. New Game')
    print('2. Quit')
    print()

    choice = input("Make selection: ")
    if choice == '2': ##exit
        exit = True
        classes.clear_screen()
    elif choice == '1': ##select multi or bot
        classes.clear_screen()
        classes.multiplayer()
    else:
        print('Invalid input')
