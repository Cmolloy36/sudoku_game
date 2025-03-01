import unittest
import numpy as np

import create_grids
from sudoku_objects import *


class TestGrid(unittest.TestCase):
    def test_in_row_cell_box(self):
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

        game_grid.update_cell_val(1,'00')

        self.assertEqual(game_grid.grid[0][0],1)

        self.assertTrue(game_grid.in_box(1,'00'))
        self.assertTrue(game_grid.in_box(1,'22'))
        self.assertFalse(game_grid.in_box(1,'03'))
        
        self.assertTrue(game_grid.in_row(1,'00'))
        self.assertTrue(game_grid.in_row(1,'08'))
        self.assertFalse(game_grid.in_row(1,'20'))

        self.assertTrue(game_grid.in_col(1,'00'))
        self.assertTrue(game_grid.in_col(1,'80'))
        self.assertFalse(game_grid.in_col(1,'02'))

        self.assertFalse(game_grid.is_valid_val(1,'12'))
        self.assertTrue(game_grid.is_valid_val(2,'12'))
        

    def test_solve_basic(self):
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
        game_grid.solve()

        self.assertFalse(0 in game_grid.grid)

        for i in range(9):
            self.assertEqual(game_grid.row_constraints[i], set(range(1,10)))
            self.assertEqual(game_grid.col_constraints[i], set(range(1,10)))
            self.assertEqual(game_grid.box_constraints[i], set(range(1,10)))

    def test_solve_reverse(self):
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
        game_grid.solve(reverse=False)

        self.assertFalse(0 in game_grid.grid)

        for i in range(9):
            self.assertEqual(game_grid.row_constraints[i], set(range(1,10)))
            self.assertEqual(game_grid.col_constraints[i], set(range(1,10)))
            self.assertEqual(game_grid.box_constraints[i], set(range(1,10)))


    def test_create_unique_grid(self):
        game_grid = Grid(Grid.default_grid)
        
        game_grid.create_unique_grid(verbose=False)

        sol1_obj = Grid(game_grid.grid.copy())
        sol2_obj = Grid(game_grid.grid.copy())

        # sol1_obj = copy.copy(game_grid)
        # sol2_obj = copy.copy(game_grid)
        sol1_obj.solve(verbose=False,reverse=False) # not solving for some reason
        sol2_obj.solve(verbose=False,reverse=True)

        self.assertTrue(np.array_equal(sol1_obj.grid, sol2_obj.grid))

    
    def test_create_valid_grid(self):
        game_grid = Grid()

        game_grid.grid = create_grids.create_valid_grid()

        game_grid.solve(reverse=False)

        self.assertFalse(0 in game_grid.grid)

        for row in range(game_grid.grid.shape[0]):
            row_set = set(game_grid.grid[row])
            self.assertEqual(row_set,{1,2,3,4,5,6,7,8,9})

        for col in range(game_grid.grid.shape[1]):
            col_set = set(game_grid.grid[col])
            self.assertEqual(col_set,{1,2,3,4,5,6,7,8,9})