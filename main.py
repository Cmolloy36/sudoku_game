from sudoku_objects import *

def main():
    
    game_grid = Grid()
    game_grid.add_cell_val(1,'00')
    
    game_grid.solve()
    print(game_grid)
    

if __name__ == '__main__':
    main()