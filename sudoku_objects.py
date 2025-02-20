import numpy as np


class Cell(object):
    'Single, 1x1, cell. Has a value, used to build 3x3 boxes and 9x9 grids'
    def __init__(self,x=None,y=None,val=None):
        '''
        val = the value of the cell
        '''
        self.x = x
        self.y = y
        self.val = val

    def update_val(self,new_val):
        'Update cell value'
        self.val = new_val

    def __eq__(self,oth):
        if self.val == oth.val:
            return True
        

class Box(object):
    def __init__(self,size=3):
        '''
        3x3 box, 9 of these in a grid
        pos = a tuple representing position (row, col)
        '''
        super().__init__(3)

        self.vals = set()
        
           
    def in_box(self,val):
        if val in self.vals:
            return True
        return False
    
    def update_box_set(self,val):
        self.vals.add(val)


class Grid(object):
    '''
    full 9x9 sudoku grid
    '''
    def __init__(self, size=9):
        self.grid = np.zeros((9,9))
        self.box_sets = np.empty((3,3),dtype=object)
        
        for i in range(3):
            for j in range(3):
                self.box_sets[i, j] = set()

        # self.grid = [[],[],[]]
        # for i in range(3):
        #     for j in range(3):
        #         self.grid[i][j] = Box(i, j)

    def __repr__(self):
        return f"{self.grid}"

    def in_row(self,val,row):
        if val in self.grid[row]:
            return True
        return False

    def in_col(self,val,col):
        if val in self.grid[:,col]:
            return True
        return False
    
    def in_box(self,val,row,col):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(row,col)
        if val in self.box_sets[box_row][box_col]:
            return True
        return False
    
    def add_cell_val(self,val,row,col):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(row,col)
        self.box_sets[box_row][box_col].add(val)
        self.grid[row,col] = val

    def remove_cell_val(self,row,col):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(row,col)
        self.box_sets[box_row][box_col].discard(self.grid[row,col])
        self.grid[row,col] = 0 # or None: need to figure out which is more difficult to display
    

    def set_initial_vals(self,initial_vals):
        pass



def convert_coord_to_box(row,col):
    'Only care about 0-8'
    box_row, cell_row = row // 3, row % 3
    box_col, cell_col = col // 3, col % 3
    return box_row, box_col, cell_row, cell_col
    # Use this twice: grid pos (8,0) will generate (2,2), (0,0). 
    # Use first eles as grid idx, second eles as pos idx (2,0), (2,0)

    # use dynamic programming to optimize: just have nums as base 3 in general?
