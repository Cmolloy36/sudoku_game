import argparse
import sys

import create_grids
from play_game import play_game_cli, play_game_gui
from sudoku_objects import *
from window import *
from draw_grid import *


'''
CLI Args should be:
args[0] = fnm
args[1] = cli or window
args[2] = if cli, difficulty
args[3] = verbose, 'true' or 'false'
'''

def main():
    parser = parser_fcn(sys.argv[1:]) 
    args = parser.parse_args()

    play_game = True
    

    if args.interface == 'CLI':
        while play_game:
            game_grid = create_grids.initialize_game_grid(args)
            play_game = play_game_cli(args,game_grid)


    if args.interface == 'GUI':
        x_margin = 100
        y_margin = 50
        cell_size = 100
        screen_x = cell_size * 9 + 2 * x_margin
        screen_y = cell_size * 9 + 2 * y_margin
        win = Window(screen_x, screen_y,x_margin,y_margin)

        
        game_gui = SudokuUI(args,win)
        win.start()
        

        # while play_game:
        #     game_grid = create_grids.initialize_game_grid(args)
        #     play_game = play_game_gui(args,game_grid)
            
    
    print('Goodbye!')



def parser_fcn(args):
    parser = argparse.ArgumentParser(prog='sudoku_game')
    parser.add_argument('-v','--verbose',action='store_true', help='Solve in verbose mode')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-i','--interface', choices=['CLI','GUI'], default='GUI', help='Play in CLI or GUI mode')

    parser.add_argument('-d','--difficulty', choices=['easy', 'medium', 'hard', 'expert'], required=False, default = 'medium', help='Set game difficulty')

    return parser


if __name__ == '__main__':
    main()