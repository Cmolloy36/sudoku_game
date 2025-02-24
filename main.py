import sys
import argparse
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

    grid = np.array([
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0]]
    )

    game_grid = Grid(grid)
    game_grid.solve(verbose,reverse=True)
    

if __name__ == '__main__':
    main()