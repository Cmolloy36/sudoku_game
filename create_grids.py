import copy

from sudoku_objects import *
                
def create_valid_grid():
    grid_obj = Grid(Grid.empty_grid)
    # print(grid_obj)
    coordlist = list(grid_obj.coords)
    # random.shuffle(coordlist)
    # print(coordlist)

    while len(coordlist) > 0:
        temp_obj = Grid(grid_obj.grid.copy())

        c_list = []
        coord = coordlist.pop(0)

        for i in range(1,10):
            if temp_obj.is_valid_val(i,coord):
                c_list.append(i)
        # print(f"coord: {coord}: {c_list}")
        val = random.choice(c_list)
        temp_obj.update_cell_val(val,coord)

        if temp_obj.solve():
            grid_obj.update_cell_val(val,coord)
            continue
        else:
            grid_obj.reset_cell_val(coord)
            coordlist.append(coord)

    return temp_obj.grid
