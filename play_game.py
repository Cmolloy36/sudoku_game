import sys
import re

from sudoku_objects import *
from create_grids import create_valid_grid


def play_game_cli(args,game_grid):
    

    while True:
        play_or_solve = input('Enter "play" or "solve" to continue. Enter "quit" to exit. ')

        if play_or_solve == 'solve':
            print('Solved grid:')
            game_grid.solve(args.verbose)

            if not args.verbose:
                print(game_grid.grid)
            
            print("\nWould you like to play again?")
            play_again = input('Enter "yes" or "no" here: ')

            return True if play_again == 'yes' else False

        elif play_or_solve == 'quit':
            print('Goodbye!')
            sys.exit()
        elif play_or_solve == 'play':

            while True:
                user_input = input("Please enter a command: ")
                coord_pattern = re.compile(r"\([1-9],[1-9]\) = [1-9]")

                if user_input == 'quit':
                    print('Goodbye!')
                    sys.exit()
                elif user_input == 'help':
                    print('''\nOptions:
    (<row>,<col>) = val: enter the row (1-9), column (1-9), and value (1-9)
    solve: solve the current grid 
    help: see what commands you have available
    quit: exit the program
        ''')

                elif user_input == 'solve':
                    game_grid.solve(args.verbose)
                    print(game_grid.grid)
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
            play_again = input('Enter "yes" or "no" here: ')

            return True if play_again == 'yes' else False

        else:
            print("Please enter a valid command.")


def play_game_gui(args,game_grid):
    pass