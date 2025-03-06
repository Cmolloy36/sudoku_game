from tkinter import *
from window import *
from sudoku_objects import *
import create_grids
import numpy as np

class SudokuUI(Frame):
    def __init__(self, args, parent):
        self.game_grid = create_grids.initialize_game_grid(args)
        self.text_idx = [[None for _ in range(9)] for _ in range(9)]
        print(self.text_idx)
        self.parent = parent # parent window
        Frame.__init__(self, parent.get_root())

        self.row, self.col = 0, 0

        self.__initUI()

    
    def __initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=self.parent.get_screen_x(),
                             height=self.parent.get_screen_y())
        self.canvas.pack(fill=BOTH, side=TOP)
        # clear_button = Button(self,
        #                       text="Clear answers",
        #                       command=self.__clear_answers)
        # clear_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_initial_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)
        self.canvas.bind("<BackSpace>", self.__delete_cell_val)


    def __draw_grid(self):
        for ele in range(10):
            line_width = 4 if ele % 3 == 0 else 2

            x0 = self.parent.get_x_margin() + ele * self.parent.get_cell_size()
            y0 = self.parent.get_y_margin()
            x1 = self.parent.get_x_margin() + ele * self.parent.get_cell_size()
            y1 = self.parent.get_screen_y() - self.parent.get_y_margin()
            
            self.canvas.create_line(x0, y0, x1, y1, width=line_width)

            x0 = self.parent.get_x_margin()
            y0 = self.parent.get_y_margin() + ele * self.parent.get_cell_size()
            x1 = self.parent.get_screen_x() - self.parent.get_x_margin()
            y1 = self.parent.get_y_margin() + ele * self.parent.get_cell_size()

            self.canvas.create_line(x0, y0, x1, y1, width=line_width)


    def __draw_initial_puzzle(self):
        self.canvas.delete("original numbers")
        self.canvas.delete("user input numbers")
        indices = np.where(self.game_grid.grid != DEFAULT)

        print(self.game_grid.grid)
        print(indices)

        for i in range(len(indices[0])):
            self.row = indices[0][i]
            self.col = indices[1][i]
            self.text_idx[self.row][self.col] = self.__draw_cell('original numbers')
            print(self.text_idx)

        non_indices = np.where(self.game_grid.grid == DEFAULT)

        for i in range(len(non_indices[0])):
            self.row = non_indices[0][i]
            self.col = non_indices[1][i]
            self.text_idx[self.row][self.col] = self.__draw_cell('user input')

        print(self.text_idx)


    def __draw_cell(self,tag=None):
        print(self.row,self.col)
        if self.text_idx[self.row][self.col] != None:
            self.canvas.delete(self.text_idx[self.row][self.col])

        x = self.parent.get_x_margin() + (self.col - 1) * self.parent.get_cell_size() + self.parent.get_cell_size() / 2
        y = self.parent.get_y_margin() + (self.row - 1) * self.parent.get_cell_size() + self.parent.get_cell_size() / 2
        color = "black"

        if not tag:
            tag = 'user input'

        return self.canvas.create_text(
            x, y, text=self.game_grid.grid[self.row][self.col], tags=tag, fill=color
        )

    def __delete_cell_val(self):
        if self.text_idx[self.row][self.col] != None:
            self.game_grid.grid[self.row][self.col] = DEFAULT
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
            row = (y - self.parent.get_y_margin()) / self.parent.get_cell_size()
            col = (x - self.parent.get_x_margin()) / self.parent.get_cell_size()

            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game_grid.puzzle[row][col] == 0:
                self.row, self.col = row, col

        self.__draw_cursor()

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = self.parent.get_x_margin() + self.col * self.parent.get_cell_size() + 1
            y0 = self.parent.get_y_margin() + self.row * self.parent.get_cell_size() + 1
            x1 = self.parent.get_x_margin() + (self.col + 1) * self.parent.get_cell_size() - 1
            y1 = self.parent.get_y_margin() + (self.row + 1) * self.parent.get_cell_size() - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                fill= "dodger blue", tags="cursor", color="black", width=3
            )

    def __key_pressed(self,event):
        if self.row >= 0 and self.col >= 0:
            if event.char in "1234567890":
                self.game_grid.grid[self.row][self.col] = int(event.char)
                self.col, self.row = -1, -1
                self.__draw_cell()
                # self.__draw_cursor() # this just deletes the cursor. Not sure I like it.
                # if self.check_win():
                #     self.__draw_victory()
