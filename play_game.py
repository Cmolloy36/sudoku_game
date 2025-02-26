from sudoku_objects import *
from create_grids import create_valid_grid

def play_game(args):
    game_grid = Grid(Grid.empty_grid)
    # print(game_grid.grid)

    game_grid.grid = create_valid_grid(args.verbose)
    # print(game_grid.grid)

    game_grid.create_unique_grid(args.verbose,args.difficulty)
    print('Creating unique grid...')
    print(game_grid.grid)

    game_grid.solve(args.verbose)
    print(game_grid.grid)