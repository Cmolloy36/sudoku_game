import sys
import re

from sudoku_objects import *
from create_grids import create_valid_grid


def play_game_cli(args,game_grid):
    base_grid = game_grid.grid.copy()
    

    while True:
        play_or_solve = play_q()

        if play_or_solve == 'solve':
            print('Solved grid:')
            game_grid.solve(args.verbose)

            if not args.verbose:
                print(game_grid.grid)
            
            print("\nWould you like to play again?")
            while True:
                play_again = play_again_q()

                if play_again == 'yes':
                    return True  
                elif play_again == 'no':
                    return False
                else:
                    print('Please enter a valid command')

        elif play_or_solve == 'quit':
            print('Goodbye!')
            sys.exit()

        elif play_or_solve == 'play':

            while True:
                user_input = command_q()
                coord_pattern = re.compile(r"\([1-9],[1-9]\) = [1-9]")

                if user_input == 'quit':
                    print('Goodbye!')
                    sys.exit()
                elif user_input == 'help':
                    print('''\nOptions:
    (<row>,<col>) = val: enter the row (1-9), column (1-9), and value (1-9)
    answer: get the answer of the current grid
    help: see what commands you have available
    quit: exit the program
        ''')

                elif user_input == 'answer':
                    game_grid.grid = base_grid
                    game_grid.solve(args.verbose)
                    break

                elif coord_pattern.match(user_input):
                    val = int(user_input[-1])
                    coord = str(int(user_input[1]) - 1) + str(int(user_input[3]) - 1)

                    if game_grid.is_valid_val(val,coord):
                        print('Good job!')
                        game_grid.update_cell_val(val,coord)
                    else:
                        print('Incorrect value! Try again.')
                    print(game_grid.grid)

                else:
                    print("Please enter a valid command.")

            print('Solved grid:')
            print(game_grid.grid)

            print("\nWould you like to play again?")
            while True:
                play_again = play_again_q()

                if play_again == 'yes':
                    return True  
                elif play_again == 'no':
                    return False
                else:
                    print('Please enter a valid command')

        else:
            print("Please enter a valid command.")


def play_q():
    return input('Enter "play" or "solve" to continue. Enter "quit" to exit. ')

def command_q():
    return input("Please enter a command: ")

def play_again_q():
    return input('Enter "yes" or "no" here: ')



def play_game_gui(args,game_grid):
    pass