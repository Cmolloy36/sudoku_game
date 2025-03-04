from tkinter import *
from window import *
import create_grids

class SudokuUI(Frame):
    def __init__(self, args, parent):
        self.game_grid = create_grids.initialize_game_grid(args)
        self.parent = parent # parent window
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    
    def __initUI(self):
        self.parent.title("Sudoku Game")
        self.pack(fill='BOTH', expand=1)
        self.canvas = Canvas(self,
                             width=800,
                             height=600)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear answers",
                              command=self.__clear_answers)
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)


    def __draw_grid(self):
        for row in range(10):
            width = 4 if row % 3 == 0 else 2

            
