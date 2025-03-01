import unittest
import mock
import sys
import numpy as np

import create_grids
import play_game
from sudoku_objects import *
from main import parser_fcn

# Updating

class TestGrid(unittest.TestCase):
    @mock.patch('play_game.play_q',return_value='play')
    def test_play_solve(self):
        testargs = ["sudoku_game", "-v", "--CLI"]
        with mock.patch.object(sys, 'argv', testargs):
            parser = parser_fcn(sys.argv[1:]) 
            args = parser.parse_args()
        
            game_grid = create_grids.initialize_game_grid(args)
            play_game_res = play_game.play_game_cli(args,game_grid)

            self.assertTrue(play_game_res)