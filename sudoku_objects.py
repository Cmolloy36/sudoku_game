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
                self.box_sets[i, j] = set(range(1, 10))
        
        # Store valid values for cell
        self.cell_set_dict = dict()
        self.coords = cross('012345678','012345678')
        self.set_initial_vals()

        # self.grid = [[],[],[]]
        # for i in range(3):
        #     for j in range(3):
        #         self.grid[i][j] = Box(i, j)

    def __repr__(self):
        return f"{self.grid}"

    def in_row(self,val,coord):
        row, col = convert_coord_to_box(coord)
        if val in self.grid[row]:
            return True
        return False

    def in_col(self,val,coord):
        row, col = convert_coord_to_box(coord)
        if val in self.grid[:,col]:
            return True
        return False
    
    def in_box(self,val,coord):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(coord,box=True)
        print(self.box_sets[box_row][box_col])
        if val in self.box_sets[box_row][box_col]:
            return True
        return False
    
    def add_val_to_cell_set(self,val,coord):
        row, col = convert_coord_to_box(coord)
        self.cell_set_dict[(row,col)] += str(val)

    def remove_val_from_cell_set(self,val,coord):
        row, col = convert_coord_to_box(coord)
        self.cell_set_dict[(row,col)] = self.cell_set_dict[(row,col)].replace(str(val),'')
        
    def add_cell_val(self,val,coord):
        box_row, box_col, row, col = convert_coord_to_box(coord,box=True)
        self.box_sets[box_row][box_col] = self.box_sets[box_row][box_col].discard(self.grid[row,col])
        self.grid[row,col] = str(val)

    def remove_cell_val(self,coord):
        box_row, box_col, row, col = convert_coord_to_box(coord,box=True)
        self.box_sets[box_row][box_col] += self.grid[row,col]
        self.grid[row,col] = '0' # or None: need to figure out which is more difficult to display
    
    def is_valid_val(self,val,coord):
        if (self.in_box(val,coord) or self.in_row(val,coord) or self.in_col(val,coord)):
            return False
        return True
    

    def get_digit_set(self,coord):
        digitset = self.cell_set_dict[coord] 
        for i in range(1,10):
            if not self.is_valid_val(i,coord):
                digitset = self.cell_set_dict[coord].replace(str(i),'')
        return digitset
        
        

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
        for coord in self.coords:
            self.cell_set_dict[coord] = '012345678'
            digit_set = self.get_digit_set(coord)
            self.cell_set_dict[coord] = digit_set


    def solve(self):
        
        indices = np.where(self.grid == 0)
        if indices == None:
            return True
        
        print(indices)

        # get all combos of points

        coord = str(indices[0][0]) + str(indices[1][0])
        print(coord)
        
        for i in range(1,10):
            print(i)
            if self.is_valid_val(i,coord):
                self.grid[coord[0]][coord[1]] = i
                self.box_sets
                if self.solve():
                    return True
                self.grid[coord[0]][coord[1]] = 0
        return False
            
                



def convert_coord_to_box(coord,box=False):
    'Only care about 0-8'
    row = int(coord[0])
    col = int(coord[1])
    box_row, cell_row = row // 3, row % 3
    box_col, cell_col = col // 3, col % 3
    if box: 
        return box_row, box_col, cell_row, cell_col 
    return cell_row, cell_col
    # Use this twice: grid pos (8,0) will generate (2,2), (0,0). 
    # Use first eles as grid idx, second eles as pos idx (2,0), (2,0)

    # use dynamic programming to optimize: just have nums as base 3 in general?


def cross(A, B):
    "Cross product of strings in A and strings in B."
    return tuple(a + b for a in A for b in B)