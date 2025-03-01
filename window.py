from tkinter import Tk, BOTH, Canvas

class Window(object):
    def __init__(self,width,height):
        #width and height are given in px
        self.__root = Tk()
        self.__root.title('Sudoku Game') 
        self.__canvas = Canvas(self.__root,bg='white',height=height,width=width)
        self.__canvas.pack(expand=1) #if empty, defaults to top
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def get_canvas(self):
        return self.__canvas

    def redraw(self):
        #updates window each time this is called
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        # print('window closed')

    def close(self):
        self.__running = False

    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)

class Point(object):
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

class Line(object):
    def __init__(self,point1,point2):
        self.__point1 = point1
        self.__point2 = point2
    
    def draw(self,canvas,fill_color):
        canvas.create_line(
            self.__point1.get_x(), self.__point1.get_y(), self.__point2.get_x(), self.__point2.get_y(), fill=fill_color, width=2
        )