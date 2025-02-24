import unittest
import numpy as np

from sudoku_objects import *


class TestGrid(unittest.TestCase):
    def test_add_cell(self):
        game_grid = Grid()
        row = 8
        col = 8
        val = 9

        box_row, box_col, cell_row, cell_col = convert_coord_to_box(8,8)
        
        game_grid.add_cell_val(val,row,col)

        self.assertEqual(game_grid.grid[row][col],val)
        self.assertNotEqual(game_grid.grid[row][col],val-1)
        
        self.assertEqual(game_grid.box_sets[box_row][box_col],{val})
        self.assertNotEqual(game_grid.box_sets[box_row][box_col-1],{val})


    def test_remove_cell(self):
        game_grid = Grid()
        row = 8
        col = 8
        val = 9

        row2 = 7
        col2 = 7
        val2 = 8

        box_row, box_col, cell_row, cell_col = convert_coord_to_box(8,8)

        # add 2 vals
        game_grid.add_cell_val(val,row,col)
        game_grid.add_cell_val(val2,row2,col2)

        self.assertEqual(game_grid.grid[row][col],val)
        self.assertNotEqual(game_grid.grid[row][col],val-1)
        
        self.assertEqual(game_grid.box_sets[box_row][box_col],{val,val2})
        self.assertNotEqual(game_grid.box_sets[box_row][box_col-1],{val,val2})

        # remove first val
        game_grid.remove_cell_val(row,col)

        self.assertEqual(game_grid.grid[row][col],0) # may change to None
        self.assertEqual(game_grid.box_sets[box_row][box_col],{val2})

        game_grid.remove_cell_val(row2,col2)

        self.assertEqual(game_grid.grid[row2][col2],0) # may change to None
        self.assertEqual(game_grid.box_sets[box_row][box_col],set())

    def test_in_box(self):
        game_grid = Grid()
        row = 8
        col = 8
        val = 9
        game_grid.add_cell_val(val,row,col)

        box_row, box_col, cell_row, cell_col = convert_coord_to_box(8,8)

        self.assertEqual(game_grid.box_sets[box_row][box_col],{val})

        self.assertTrue(game_grid.in_box(9,6,6))
        self.assertTrue(game_grid.in_box(9,7,7))
        self.assertTrue(game_grid.in_box(9,8,8))
        self.assertFalse(game_grid.in_box(8,8,8))
        self.assertFalse(game_grid.in_box(9,5,5))
        self.assertFalse(game_grid.in_box(9,2,2))

    def test_in_box_after_rm(self):
        game_grid = Grid()
        row = 8
        col = 8
        val = 9

        box_row, box_col, cell_row, cell_col = convert_coord_to_box(8,8)

        game_grid.add_cell_val(val,row,col)

        self.assertEqual(game_grid.box_sets[box_row][box_col],{val})

        game_grid.remove_cell_val(row,col)

        self.assertEqual(game_grid.box_sets[box_row][box_col],set())

        self.assertFalse(game_grid.in_box(val,row,col))
        self.assertFalse(game_grid.in_box(val,row,col))
        self.assertFalse(game_grid.in_box(val,row,col))
    
    def test_in_row(self):
        game_grid = Grid()
        game_grid.add_cell_val(9,8,8)
        self.assertTrue(game_grid.in_row(9,8))
        self.assertFalse(game_grid.in_row(9,7))
        self.assertFalse(game_grid.in_row(8,8))

    def test_in_col(self):
        game_grid = Grid()
        game_grid.add_cell_val(9,8,8)
        self.assertTrue(game_grid.in_col(9,8))
        self.assertFalse(game_grid.in_col(9,7))
        self.assertFalse(game_grid.in_col(8,8))
        