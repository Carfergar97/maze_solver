import time
from graphics import Cell

class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = [ ]
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        
        self._cells = [[Cell(self._win) for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        if self._win == None:
            return
        cell_x1 = self._x1 + self._cell_size_x*j
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = self._y1 + self._cell_size_y*i
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)