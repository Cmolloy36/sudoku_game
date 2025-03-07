from tkinter import *
from window import *
from sudoku_objects import *
import create_grids
import numpy as np

class SudokuUI(Frame):
    def __init__(self, args, parent):
        
        self.parent = parent # parent window
        self.canvas = parent.get_canvas()
        self.args = args
        Frame.__init__(self, parent.get_root())

        self.row, self.col = -1, -1

        self.__initUI()
        self.__new_game()

    
    def __initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canvas.pack(fill=BOTH, side=TOP)

        self.__draw_grid()
        
        solve_button = Button(self, text="Solve Puzzle", command=self.__solve_puzzle)
        solve_button.pack(fill=BOTH, side=BOTTOM)
        
        clear_button = Button(self, text="Clear Answers", command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.new_button = Button(self, text="New Game", command=self.__new_game)
        self.new_button.pack(side=LEFT, padx=5)


        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)
        self.canvas.bind("<BackSpace>", self.__delete_cell_val)


    def __new_game(self):
        self.game_grid = create_grids.initialize_game_grid(self.args)
        self.text_idx = [[None for _ in range(9)] for _ in range(9)]
        self.orig_vals = self.game_grid.grid.copy()
        self.canvas.delete("original numbers")
        self.__draw_initial_puzzle()

    def __draw_grid(self):
        self.canvas.delete("grid_lines")
        for ele in range(10):
            line_width = 4 if ele % 3 == 0 else 2

            x0 = self.parent.get_x_margin() + ele * self.parent.get_cell_size()
            y0 = self.parent.get_y_margin()
            x1 = self.parent.get_x_margin() + ele * self.parent.get_cell_size()
            y1 = self.parent.get_screen_y() - self.parent.get_y_margin()
            
            self.canvas.create_line(x0, y0, x1, y1, width=line_width, tag="grid_lines")

            x0 = self.parent.get_x_margin()
            y0 = self.parent.get_y_margin() + ele * self.parent.get_cell_size()
            x1 = self.parent.get_screen_x() - self.parent.get_x_margin()
            y1 = self.parent.get_y_margin() + ele * self.parent.get_cell_size()

            self.canvas.create_line(x0, y0, x1, y1, width=line_width, tag="grid_lines")


    def __draw_initial_puzzle(self,color='black'):
        
        self.canvas.delete("user input numbers")
        
        for row in range(9):
            for col in range(9):
                self.row, self.col = row, col
                val = self.game_grid.grid[row][col]
                if val != DEFAULT:
                    self.__draw_cell(tag='original numbers')

        print(self.game_grid.grid)
        self.row, self.col = -1, -1
        print('Done generating puzzle!')


    def __solve_puzzle(self):
        solver = Grid(self.game_grid.grid.copy())
        if solver.solve():
            self.game_grid.grid = solver.grid
            self.__draw_initial_puzzle()
            self.game_over = True


    def __draw_cell(self,tag=None):
        # print(self.row,self.col)
        # if self.orig_vals[self.row][self.col] == DEFAULT:
        if self.text_idx[self.row][self.col] != None:
            self.__delete_cell_val()

        x = self.parent.get_x_margin() + (self.col) * self.parent.get_cell_size() + self.parent.get_cell_size() / 2
        y = self.parent.get_y_margin() + (self.row) * self.parent.get_cell_size() + self.parent.get_cell_size() / 2

        if tag == 'original numbers':
            color = "black"
        else:
            color = "dodger blue"

        print('created text')

        self.text_idx[self.row][self.col] = self.canvas.create_text(
            x, y, text=self.game_grid.grid[self.row][self.col], tags=tag, fill=color, font=("Arial", 40)
        )

        print(self.text_idx[self.row][self.col])
        
        return self.text_idx[self.row][self.col]

    def __delete_cell_val(self,event=None):
        print('deleting text')
        print(self.text_idx[self.row][self.col])
        if self.text_idx[self.row][self.col] != None:
            self.game_grid.grid[self.row][self.col] = DEFAULT


            if self.text_idx[self.row][self.col]:
                print(self.text_idx[self.row][self.col])
                self.canvas.delete(self.text_idx[self.row][self.col])
                self.text_idx[self.row][self.col] = None


    def __cell_clicked(self, event):
        if self.game_grid.game_over:
            return
        x, y = event.x, event.y
        if (self.parent.get_x_margin() < x < self.parent.get_screen_x() - self.parent.get_x_margin() and 
            self.parent.get_y_margin() < y < self.parent.get_screen_y() - self.parent.get_x_margin()):

            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row = (y - self.parent.get_y_margin()) // self.parent.get_cell_size()
            col = (x - self.parent.get_x_margin()) // self.parent.get_cell_size()

            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.orig_vals[row][col] == DEFAULT:
                self.row, self.col = row, col
                print(self.row,self.col)
                print(self.text_idx[self.row][self.col])

        self.__draw_cursor()

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = self.parent.get_x_margin() + self.col * self.parent.get_cell_size() + 1
            y0 = self.parent.get_y_margin() + self.row * self.parent.get_cell_size() + 1
            x1 = self.parent.get_x_margin() + (self.col + 1) * self.parent.get_cell_size() - 1
            y1 = self.parent.get_y_margin() + (self.row + 1) * self.parent.get_cell_size() - 1
            self.canvas.create_rectangle(
                x0-1, y0-1, x1, y1,
                outline='red', tags="cursor", width=3
            )

    def __key_pressed(self,event):
        if self.row >= 0 and self.col >= 0:
            if event.char in "123456789":
                self.__delete_cell_val()
                self.game_grid.grid[self.row][self.col] = int(event.char)
                self.text_idx[self.row][self.col] = self.__draw_cell(tag='user input numbers')
                print(self.text_idx[self.row][self.col])
                self.col, self.row = -1, -1
                # self.__draw_cursor() # this just deletes the cursor. Not sure I like it.
                # if self.check_win():
                #     self.__draw_victory()


    def __clear_answers(self):
        # Reset to original puzzle
        self.game_grid.grid = self.orig_vals.copy()
        self.__draw_initial_puzzle()
        self.game_over = False
