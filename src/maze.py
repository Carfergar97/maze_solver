import time
from graphics import Cell

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