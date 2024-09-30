from tkinter import Tk, BOTH, Canvas
from graphics import Line
from maze import Maze
class Window():
    def __init__(self, widht:int, height:int) -> None:

        self._root = Tk()
        self._root.title("My_window")
        self._canvas = Canvas(self._root,bg = "white", width=widht, height=height)
        self._canvas.pack()
        self._window_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    
    def wait_for_close(self):
        self._window_running = True
        while self._window_running == True:
            self.redraw()
    
    def close(self):
        self._window_running = False

    def draw_line(self,line:Line, fill_color:str):
        line.draw(self._canvas, fill_color)
