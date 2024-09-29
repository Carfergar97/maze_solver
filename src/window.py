from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
class Window():
    def __init__(self, widht:int, height:int) -> None:

        self.__root = Tk()
        self.__root.title("My_window")
        self.__canvas = Canvas(self.__root,bg = "white", width=widht, height=height)
        self.__canvas.pack()
        self.__window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running == True:
            self.redraw()
    
    def close(self):
        self.__window_running = False

    def draw_line(self,line:Line, fill_color:str):
        line.draw(self.__canvas, fill_color)
if __name__=="__main__":
    win = Window(800,600)
    win.draw_line(Line(Point(0,0),Point(800,600)), "red")
    win.wait_for_close()