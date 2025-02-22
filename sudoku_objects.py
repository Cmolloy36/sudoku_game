import numpy as np
import random
import itertools

class Grid(object):
    '''
    full 9x9 sudoku grid
    '''
    def __init__(self, size=9):
        self.grid = np.zeros((9,9))
        self.box_sets = np.empty((3,3),dtype=object)
        
        for i in range(3):
            for j in range(3):
                self.box_sets[i, j] = '123456789'
        
        # Store valid values for cell
        self.cell_set_dict = dict()
        limits = range(1, 10)
        permutations = list(itertools.product(limits, repeat=2))
        self.permutations = permutations
        self.set_initial_vals()

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
    
    def add_val_to_cell_set(self,val,row,col):
        self.cell_set_dict[(row,col)] += val

    def remove_val_from_cell_set(self,val,row,col):
        self.cell_set_dict[(row,col)] = self.cell_set_dict[(row,col)].replace(val,'')
        
    def add_cell_val(self,val,row,col):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(row,col)
        self.box_sets[box_row][box_col] = self.box_sets[box_row][box_col].replace(self.grid[row,col], '')
        self.grid[row,col] = val

    def remove_cell_val(self,row,col):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(row,col)
        self.box_sets[box_row][box_col] += self.grid[row,col]
        self.grid[row,col] = 0 # or None: need to figure out which is more difficult to display
    
    def is_valid_val(self,val,coord):
        if any(self.in_box(val,coord[0],coord[1]),self.in_row(val,coord[0]),self.in_col(val,coord[1])):
            return False
        return True
    
    def get_digit_set(self,coord):
        for i in range(1,10):
            if self.is_valid_val(i,coord):



            
        

    def solve(self,val,coord):
        # if invalid number
        pass
        
        
        

    def set_initial_vals(self,seed=random.randint(0,100000)):
        random.seed(seed)
        '''
        self.grid = np.array(
            [1,2,3,  4,5,6,  7,8,9],
            [4,5,6,  7,8,9,  1,2,3],
            [7,8,9,  1,2,3,  4,5,6],

            [2,3,1,  5,6,4,  8,9,7],
            [5,6,4,  8,9,7,  2,3,1],
            [8,9,7,  2,3,1,  5,6,4],

            [3,1,2,  6,4,5,  9,7,8],
            [6,4,5,  9,7,8,  3,1,2],
            [9,7,8,  3,1,2,  6,4,5]
        )
        '''
        for perm in self.permutations:
            digit_set = 
            self.cell_set_dict[perm] = '123456789'


    def solve(self):

        indices = np.where(self.grid == 0)

        # get all combos of points
        
        
        while 0 in self.grid:
            coord = random.choice(permutations)
            for val in self.cell_set_dict[coord]:
               self.is_valid_coord(val,coord)


            
                



def convert_coord_to_box(row,col):
    'Only care about 0-8'
    box_row, cell_row = row // 3, row % 3
    box_col, cell_col = col // 3, col % 3
    return box_row, box_col, cell_row, cell_col
    # Use this twice: grid pos (8,0) will generate (2,2), (0,0). 
    # Use first eles as grid idx, second eles as pos idx (2,0), (2,0)

    # use dynamic programming to optimize: just have nums as base 3 in general?

