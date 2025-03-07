from tkinter import Tk, Frame, BOTH, Canvas

class Window(object):
    def __init__(self,width,height,x_margin=100,y_margin=50,cell_size=100):
        #width and height are given in px
        self.__root = Tk()
        self.__root.title('Sudoku Game') 

        self.x_margin = x_margin
        self.y_margin = y_margin
        self.cell_size = cell_size
        self.screen_x = cell_size * 9 + 2 * x_margin
        self.screen_y = cell_size * 9 + 2 * y_margin

        self.__frame = Frame(self.__root)
        self.__frame.pack(fill=BOTH, expand=1)
        
        self.__canvas = Canvas(self.__root,bg='white',height=self.screen_y,width=self.screen_x)
        self.__canvas.pack(fill=BOTH, expand=1)
        
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def get_canvas(self):
        return self.__canvas
    
    def get_x_margin(self):
        return self.x_margin
    
    def get_y_margin(self):
        return self.y_margin
    
    def get_cell_size(self):
        return self.cell_size
    
    def get_screen_x(self):
        return self.screen_x
    
    def get_screen_y(self):
        return self.screen_y
    
    def get_root(self):
        return self.__root

    def start(self):
        self.__root.mainloop()

    def redraw(self):
        #updates window each time this is called
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.__running = False
        self.__root.destroy()