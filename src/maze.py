import time
from graphics import Cell
import random
class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed = None):
        self._cells = [ ]
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if(seed != None):
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        
        self._cells = [[Cell(self._win) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        if self._win == None:
            return
        cell_x1 = self._x1 + self._cell_size_x*i
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = self._y1 + self._cell_size_y*j
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i - 1 >= 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append((i-1,j))
            if i + 1 < self._num_cols:
                if self._cells[i+1][j].visited == False:
                    to_visit.append((i+1,j))
            if j - 1 >= 0:
                if self._cells[i][j - 1].visited == False:
                    to_visit.append((i,j - 1))
            if j + 1 < self._num_rows:
                if self._cells[i][j + 1].visited == False:
                    to_visit.append((i,j + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            next = random.randrange(len(to_visit))
            if to_visit[next][0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if to_visit[next][0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if to_visit[next][1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if to_visit[next][1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            self._break_walls_r(to_visit[next][0],to_visit[next][1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i:int,j:int)->bool:
        
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        
        if i - 1 >= 0 and self._cells[i][j].has_left_wall == False and self._cells[i - 1][j].visited==False:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1,j)==True:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j],True) 
       
        if (i + 1 < self._num_cols) and (self._cells[i][j].has_right_wall == False) and (self._cells[i + 1][j].visited==False):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1,j)==True:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j],True) 

        if j - 1 >= 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i,j - 1)==True:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1],True) 
        
        if j + 1 < self._num_rows and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i,j + 1)==True:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1],True) 
        return False