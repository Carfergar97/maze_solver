from tkinter import Canvas
import time

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1:Point, p2:Point) -> None:
        self.__p1 = p1
        self.__p2 = p2

    def draw(self,canvas:Canvas,fill_color:str):
        canvas.create_line(self.__p1.x,self.__p1.y, self.__p2.x,self.__p2.y,fill=fill_color, width=2)

class Cell():
    def __init__(self,win) -> None:
        
        self.has_left_wall = True 
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True 
        self.__x1 = None 
        self.__x2 = None 
        self.__y1 = None 
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        if self.has_left_wall == True:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),"black")
        
        if self.has_right_wall == True:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),"black")
        
        if self.has_top_wall == True:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),"black")

        if self.has_bottom_wall == True:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),"black")

    def draw_move(self, to_cell, undo:bool = False):
        color = "red" if undo == True else "gray"
        self.__win.draw_line(Line(self.get_center(), to_cell.get_center()) ,color)    

    def get_center(self):
        return Point(self.__x1 + (self.__x2 - self.__x1)/2, self.__y1 + (self.__y2 - self.__y1)/2)

class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create__cells()

    def __create__cells(self):
        
        self.__cells = [[Cell(self.__win) for _ in range(self.__num_cols)] for _ in range(self.__num_rows)]
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self.__draw__cell(i,j)

    def __draw__cell(self,i,j):
        cell_x1 = self.__x1 + self.__cell_size_x*j
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y1 = self.__y1 + self.__cell_size_y*i
        cell_y2 = cell_y1 + self.__cell_size_y
        self.__cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
