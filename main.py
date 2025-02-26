import argparse

import create_grids
from play_game import play_game
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
    group.add_argument('--GUI', action='store_true', help='Play in GUI mode')

    parser.add_argument('--difficulty', choices=['easy', 'medium', 'hard', 'expert'], required=False, default = 'medium', help='Set game difficulty')

    args = parser.parse_args()

    play_game(args)

    # game_grid = Grid(Grid.empty_grid)
    # # print(game_grid.grid)

    # game_grid.grid = create_grids.create_valid_grid(args.verbose)
    # # print(game_grid.grid)

    # game_grid.create_unique_grid(args.verbose,args.difficulty)
    # print('Creating unique grid...')
    # print(game_grid.grid)

    # game_grid.solve(args.verbose)
    # print(game_grid.grid)

    

if __name__ == '__main__':
    main()