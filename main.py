import sys
import argparse

import create_grids
from sudoku_objects import *


"""
CLI Args should be:
args[0] = fnm
args[1] = cli or window
args[2] = if cli, difficulty
args[3] = verbose, "true" or "false"
"""

def main():

    #argparse stuff here


    verbose = False

    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        fnm = sys.argv[0]
        verbose = sys.argv[1]

    game_grid = Grid(Grid.empty_grid)
    # game_grid.grid = create_grids.create_valid_grid()
    # game_grid.create_unique_grid()
    game_grid.solve()
    print(game_grid)
    

if __name__ == '__main__':
    main()