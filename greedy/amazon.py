# GAME OF LIFE

"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.
"""


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
rows = len(board)
cols = len(board[0])

# create temp array

# temp = [[0]*cols for i in range(rows)]
def gameoflife(board):
    for r in range(rows):
        for c in range(cols):
            board[r][c] = helper(r,c)
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2:
                board[r][c] = 0
            elif board[r][c] == -1:
                board[r][c] = 1
    
            
            
def helper(r,c):
    count = 0
    dir = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
    
    for x,y in dir:
        if 0<=r+y<rows and 0<=c+x<cols and board[r+y][c+x] >0:
            count += 1
        
    if board[r][c] > 0:
        if count < 2:
            return 2
        elif count ==2  or count == 3:
            return 1
        else:
            return 2
    else:
        if count == 3:
            return -1
        else:
            return 0
    
gameoflife(board)
print(board)

# create a helper function to keep track of comparisonsoard