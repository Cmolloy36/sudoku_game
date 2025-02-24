import numpy as np
import random

DEFAULT = 0

'''

'''

class Grid(object):
    '''
    full 9x9 sudoku grid
    '''

    default_grid = np.array([
                [1,2,3,  4,5,6,  7,8,9],
                [4,5,6,  7,8,9,  1,2,3],
                [7,8,9,  1,2,3,  4,5,6],

                [2,3,1,  5,6,4,  8,9,7],
                [5,6,4,  8,9,7,  2,3,1],
                [8,9,7,  2,3,1,  5,6,4],

                [3,1,2,  6,4,5,  9,7,8],
                [6,4,5,  9,7,8,  3,1,2],
                [9,7,8,  3,1,2,  6,4,5]]
                )

    def __init__(self,grid=np.empty(0)):


        self.box_sets = np.empty((3,3),dtype=object)
        
        for i in range(3):
            for j in range(3):
                self.box_sets[i, j] = set(range(1, 10)) #available values
        
        # Store valid values for cell
        self.coords = cross('012345678','012345678')

        if grid.size != 0:
            self.grid = grid
        else:
            self.grid = Grid.default_grid
            self.create_unique_grid()

        self.initialize_box_sets()

        self.count = 0
        self.valchecks = 0


    def __repr__(self):
        return f"{self.grid}"
    

    def __eq__(self,oth):
        self_grid = self.grid.flatten()
        oth_grid = oth.grid.flatten()
        for i in range(self.grid.size):
            if self_grid[i] != oth_grid[i]:
                return False
        return True

    
    def initialize_box_sets(self):
        indices = np.where(self.grid != DEFAULT)
        for i in range(len(indices[0])):
            val = self.grid[indices[0][i]][indices[1][i]]
            coord = str(indices[0][i]) + str(indices[1][i])
            self.update_box_set(val,coord)
    

    def update_cell_val(self,val,coord):
        if self.is_valid_val(val,coord):
            row, col = convert_coordstr_to_int(coord)
            self.grid[row][col] = val
            self.update_box_set(val,coord)


    def reset_cell_val(self,coord):
        row, col = convert_coordstr_to_int(coord)
        self.update_box_set(self.grid[row][col],coord)
        self.grid[row][col] = DEFAULT


    def in_row(self,val,coord):
        row, col = convert_coordstr_to_int(coord)
        if val in self.grid[row]:
            return True
        return False


    def in_col(self,val,coord):
        row, col = convert_coordstr_to_int(coord)
        if val in self.grid[:,col]:
            return True
        return False
    

    def in_box(self,val,coord):
        box_row, box_col, cell_row, cell_col = convert_coord_to_box(coord,box=True)
        # print(self.box_sets[box_row][box_col])
        if val not in self.box_sets[box_row][box_col]:
            return True
        return False
    
        
    def is_valid_val(self,val,coord):
        if (self.in_box(val,coord) or self.in_row(val,coord) or self.in_col(val,coord)):
            return False
        return True
    

    def update_box_set(self,val,coord):
        box_row, box_col, row, col = convert_coord_to_box(coord,box=True)
        # print(f"update box set: {self.box_sets[box_row][box_col]}")
        if val in self.box_sets[box_row][box_col]:
            # print(f"update box set: {self.box_sets[box_row][box_col]}")
            self.box_sets[box_row][box_col].discard(val)
        else:
            self.box_sets[box_row][box_col].add(val)


    def solve(self,verbose=False,reverse=False):
        indices = np.where(self.grid == DEFAULT) #this could be optimized to only get one
        if indices[0].size == 0:
            if verbose:
                print(f"Solved! Took {self.count} steps and {self.valchecks} value checks")
            else:
                print("Solved!")
            print(self.grid)
            return True

        # get all combos of points
        self.count += 1

        coord = str(indices[0][0]) + str(indices[1][0])

        if verbose:
            print(self.grid)
            print(f"cell: ({indices[0][0] + 1},{indices[1][0] + 1})")

        row, col = convert_coord_to_box(coord)
        
        range_obj = np.arange(1,10)
        if reverse:
            range_obj = np.arange(start=9,stop=0,step=-1)


        for i in range_obj:
            self.valchecks += 1
            if self.is_valid_val(i,coord):
                self.update_cell_val(i,coord)
                if self.solve(verbose,reverse):
                    return True
                self.reset_cell_val(coord)
        return False
    
    
    def create_unique_grid(self): # https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
        coordlist = self.coords
        random.shuffle(coordlist)

        while len(coordlist != 0):
            self.solve()

        
            
                

def convert_coordstr_to_int(coord):
    return int(coord[0]), int(coord[1])

def convert_coord_to_box(coord,box=False):
    'Only care about 0-8'
    '''
    INPUT:
    coord: 2 char string representing row_idx, col_idx
    box: bool, whether you want to return box_coords or not (if using box set implementation)
    '''
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