from sudoku_objects import *

def main():

    game_grid = Grid(default_grid)
    # game_grid.update_cell_val(1,'01')

    
    game_grid.solve()
    print('solved!')
    # print(game_grid)
    

if __name__ == '__main__':
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
    main()