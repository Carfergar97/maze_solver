from tkinter import Canvas
import time

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1:Point, p2:Point) -> None:
        self._p1 = p1
        self._p2 = p2

    def draw(self,canvas:Canvas,fill_color:str):
        canvas.create_line(self._p1.x,self._p1.y, self._p2.x,self._p2.y,fill=fill_color, width=2)

class Cell():
    def __init__(self,win) -> None:
        
        self.has_left_wall = True 
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
        self._x1 = None 
        self._x2 = None 
        self._y1 = None 
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_left_wall == True:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"black")
        
        if self.has_right_wall == True:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"black")
        
        if self.has_top_wall == True:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"black")

        if self.has_bottom_wall == True:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"black")

    def draw_move(self, to_cell, undo:bool = False):
        color = "red" if undo == True else "gray"
        self._win.draw_line(Line(self.get_center(), to_cell.get_center()) ,color)    

    def get_center(self):
        return Point(self._x1 + (self._x2 - self._x1)/2, self._y1 + (self._y2 - self._y1)/2)
