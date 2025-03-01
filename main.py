import argparse

import create_grids
from play_game import play_game_cli, play_game_gui
from sudoku_objects import *


'''
CLI Args should be:
args[0] = fnm
args[1] = cli or window
args[2] = if cli, difficulty
args[3] = verbose, 'true' or 'false'
'''

def main():
    parser = argparse.ArgumentParser(prog='sudoku_game')
    parser.add_argument('-v','--verbose',action='store_true', help='Solve in verbose mode')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--CLI', action='store_true', help='Play in CLI mode')
    # group.add_argument('--GUI', action='store_true', help='Play in GUI mode')

    parser.add_argument('-d','--difficulty', choices=['easy', 'medium', 'hard', 'expert'], required=False, default = 'medium', help='Set game difficulty')

    args = parser.parse_args()

    play_game = True

    if args.CLI:
        while play_game:
            game_grid = create_grids.initialize_game_grid(args)
            play_game = play_game_cli(args,game_grid)
            print('Goodbye!')
            
        
    # play_game_gui(args,game_grid)


if __name__ == '__main__':
    main()