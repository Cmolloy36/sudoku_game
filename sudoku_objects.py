import numpy as np
import random
import create_grids

DEFAULT = 0

class Grid(object):
    '''
    full 9x9 sudoku grid
    '''
    empty_grid = np.array([
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

    one_row_grid = np.array([
        [1,2,3,  4,5,6,  7,8,9],
        [4,5,6,  7,8,9,  1,2,3],
        [7,8,9,  1,2,3,  4,5,6],

        [2,3,1,  5,6,4,  8,9,7],
        [5,6,4,  8,9,7,  2,3,1],
        [8,9,7,  2,3,1,  5,6,4],

        [3,1,2,  6,4,5,  9,7,8],
        [6,4,5,  9,7,8,  3,1,2],
        [0,0,0,  0,0,0,  0,0,0]]
    )

    def __init__(self,grid=np.empty(0)):
        
        # Store valid values for cell
        self.coords = cross('012345678','012345678')

        self.count = 0
        self.valchecks = 0

        if grid.size != 0:
            self.grid = grid
        else:
            self.grid = Grid.empty_grid
            # self.grid = create_grids.create_valid_grid()
            # print(self.grid)
            # self.create_unique_grid()

        self.cell_possible_values = {coord: set(range(1, 10)) for coord in self.coords}
        self.row_constraints = {row: set() for row in range(9)}
        self.col_constraints = {col: set() for col in range(9)}
        self.box_constraints = {box: set() for box in range(9)}

        self.initialize_constraints()


    def __repr__(self):
        return f"{self.grid}"
    

    def __eq__(self,oth):
        if self.grid.all() == oth.grid.all(): # I don't know if this works
            return True
        return False
    

    def __copy__(self):
        return Grid(self.grid)

    
    def initialize_constraints(self):
        indices = np.where(self.grid != DEFAULT)
        for i in range(len(indices[0])):
            row = indices[0][i]
            col = indices[1][i]
            box = convert_coord_to_box(str(row)+str(col))
            print(box)
            val = self.grid[row][col]
            self.add_row_constraint(val,row)
            self.add_col_constraint(val,col)
            self.add_box_constraint(val,box)


    def add_row_constraint(self,val,row):
        self.row_constraints[row].add(val)


    def add_col_constraint(self,val,col):
        self.col_constraints[col].add(val)


    def add_box_constraint(self,val,box):
        self.box_constraints[box].add(val)


    def rm_row_constraint(self,val,row):
        self.row_constraints[row].discard(val)


    def rm_col_constraint(self,val,col):
        self.col_constraints[col].discard(val)


    def rm_box_constraint(self,val,box):
        self.box_constraints[box].discard(val)


    def in_row(self,val,coord):
        row, col = convert_coordstr_to_int(coord)
        if val in self.row_constraints[row]: # if I use not, then it becomes values that COULD be in the row
            return True
        return False


    def in_col(self,val,coord):
        row, col = convert_coordstr_to_int(coord)
        if val in self.col_constraints[col]: # if I use not, then it becomes values that COULD be in the col
            return True
        return False
    

    def in_box(self,val,coord):
        box_idx = convert_coord_to_box(coord)
        if val in self.box_constraints[box_idx]: # if I use not, then it becomes values that COULD be in the box
            return True
        return False
    
        
    def is_valid_val(self,val,coord):
        if (self.in_box(val,coord) or self.in_row(val,coord) or self.in_col(val,coord)):
            return False
        return True
    

    def update_cell_val(self,val,coord):
        if self.is_valid_val(val,coord):
            row, col = convert_coordstr_to_int(coord)
            box = convert_coord_to_box(coord)

            self.grid[row][col] = val

            self.add_row_constraint(val,row)
            self.add_col_constraint(val,col)
            self.add_box_constraint(val,box)


    def reset_cell_val(self,coord):
        row, col = convert_coordstr_to_int(coord)
        box = convert_coord_to_box(coord)

        val = self.grid[row][col]
        self.grid[row][col] = DEFAULT

        self.rm_row_constraint(val,row)
        self.rm_col_constraint(val,col)
        self.rm_box_constraint(val,box)


    # def update_box_set(self,val,coord):
    #     box_idx = convert_coord_to_box(coord)
    #     # print(f"update box set: {self.box_sets[box_row][box_col]}")
    #     if val in self.box_sets[box_row][box_col]:
    #         # print(f"update box set: {self.box_sets[box_row][box_col]}")
    #         self.box_sets[box_row][box_col].discard(val)
    #     else:
    #         self.box_sets[box_row][box_col].add(val)


    def solve(self,verbose=False,reverse=False):
        indices = np.where(self.grid == DEFAULT) #this could be optimized to only get one
        # print(len(indices[0]))
        if indices[0].size == 0:
            if verbose:
                print(f"Solved! Took {self.count} steps and {self.valchecks} value checks")
            else:
                print("Solved!")
            print(self.grid)
            return True
        
        self.count += 1

        coord = str(indices[0][0]) + str(indices[1][0])
        # print(coord)

        print(self.grid)

        if verbose:
            print(self.grid)
            print(f"cell: ({indices[0][0] + 1},{indices[1][0] + 1})")

        range_obj = np.arange(1,10)
        if reverse:
            range_obj = np.arange(start=9,stop=0,step=-1)


        for i in range_obj:
            print(f"Trying {i} at {coord}")
            self.valchecks += 1
            if self.is_valid_val(i,coord):
                self.update_cell_val(i,coord)
                if self.solve(verbose,reverse):
                    return True
                self.reset_cell_val(coord)
        return False
    
    
    def create_unique_grid(self,verbose=False): # https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
        coordlist = list(self.coords)
        random.shuffle(coordlist)


        ct = 0
        visited_coords = []

        sol1_obj = Grid(self.grid.copy())
        sol2_obj = Grid(self.grid.copy())

        while len(coordlist) != 0:
            ct += 1

            coord = coordlist.pop(0)
            if coord in visited_coords:
                return
        
            print(coord)
            print(self.grid)
            
            row, col = convert_coordstr_to_int(coord)
            val = self.grid[row][col]
            
            '''
            to implement difficulty,
            stop when self.grid.where()'''

            visited_coords.append(coord)
            self.reset_cell_val(coord)

            # indices = np.where(self.grid == DEFAULT)

            # for i in range(len(indices[0])):
            #     sol1_obj.reset_cell_val(str(indices[0][0]) + str(indices[1][0]))
            #     sol2_obj.reset_cell_val(str(indices[0][0]) + str(indices[1][0]))

            if verbose:
                print(f'count: {ct}\n')
                print(self.grid)

            sol1_obj.grid = self.grid.copy()
            sol2_obj.grid = self.grid.copy()

            sol1_obj.box_sets = self.box_sets.copy()
            sol2_obj.box_sets = self.box_sets.copy()

            # sol1_obj = copy.copy(self)
            # sol2_obj = copy.copy(self)
            sol1_obj.solve(verbose=False,reverse=False) # not solving for some reason
            sol2_obj.solve(verbose=False,reverse=True)

            # print(f'self: \n{self.grid}')
            # print(f'sol1: \n{sol1_obj.grid}')
            # print(f'sol2: \n{sol2_obj.grid}')

            if not np.array_equal(sol1_obj.grid, sol2_obj.grid):
                coordlist.append(coord)
                self.update_cell_val(val,coord)
                

        
            
                

def convert_coordstr_to_int(coord):
    return int(coord[0]), int(coord[1])

def convert_coord_to_box(coord):
    'Only care about 0-8'
    '''
    INPUT:
    coord: 2 char string representing row_idx, col_idx
    '''
    row = int(coord[0])
    col = int(coord[1])
    box_index = (row // 3) * 3 + (col // 3)
    return box_index
    # Use this twice: grid pos (8,0) will generate (2,2), (0,0). 
    # Use first eles as grid idx, second eles as pos idx (2,0), (2,0)

    # use dynamic programming to optimize: just have nums as base 3 in general?


def cross(A, B):
    "Cross product of strings in A and strings in B."
    return list(a + b for a in A for b in B)