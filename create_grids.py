import copy

from sudoku_objects import *

def create_unique_grid(verbose=False): # https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
    gt_grid = Grid(Grid.default_grid)
    
    coordlist = gt_grid.coords
    random.shuffle(coordlist)

    ct = 0
    visited_coords = []

    # sol1_obj = Grid(gt_grid.grid)
    # sol2_obj = Grid(gt_grid.grid)

    while len(coordlist) != 0:
        ct += 1

        coord = coordlist.pop(0)
        row, col = convert_coordstr_to_int(coord)
        val = gt_grid.grid[row][col]
        if coord in visited_coords:
            return
        
        '''
        to implement difficulty,
        stop when gt_grid.grid.where()'''

        visited_coords.append(coord)
        gt_grid.reset_cell_val(coord)

        # indices = np.where(gt_grid.grid == DEFAULT)

        # for i in range(len(indices[0])):
        #     sol1_obj.reset_cell_val(str(indices[0][0]) + str(indices[1][0]))
        #     sol2_obj.reset_cell_val(str(indices[0][0]) + str(indices[1][0]))

        if verbose:
            print(f'count: {ct}\n')
            print(gt_grid.grid)

        sol1_obj = Grid(gt_grid.grid.copy())
        sol2_obj = Grid(gt_grid.grid.copy())

        # sol1_obj = copy.copy(gt_grid)
        # sol2_obj = copy.copy(gt_grid)
        sol1_obj.solve(verbose=False,reverse=False) # not solving for some reason
        sol2_obj.solve(verbose=False,reverse=True)

        # print(f'gt_grid: \n{gt_grid.grid}')
        # print(f'sol1: \n{sol1_obj.grid}')
        # print(f'sol2: \n{sol2_obj.grid}')

        if not np.array_equal(sol1_obj.grid, sol2_obj.grid):
            coordlist.append(coord)
            gt_grid.update_cell_val(val,coord)
                

def create_valid_grid():
    grid_obj = Grid(Grid.empty_grid)
    # print(grid_obj)
    coordlist = list(grid_obj.coords)
    random.shuffle(coordlist)
    # print(coordlist)
    
     
    while len(coordlist) > 0:
        temp_obj = Grid(grid_obj.grid.copy())

        c_list = []
        coord = random.choice(coordlist)
        coordlist.remove(coord)

        for i in range(1,10):
            if temp_obj.is_valid_val(i,coord):
                c_list.append(i)

        val = random.choice(c_list)
        temp_obj.update_cell_val(val,coord)
        if temp_obj.solve():
            grid_obj.update_cell_val(val,coord)
            continue
        else:
            grid_obj.reset_cell_val(coord)
            # coordlist.append(coord)

    return temp_obj.grid