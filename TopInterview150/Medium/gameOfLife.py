"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):
                nei = self.count_neighbors(row, col, board)
                if board[row][col] == 1:
                    if nei in [2, 3]: # living and has 2 or 3 neighbors
                        board[row][col] = 3 # will live in the next state
                elif nei == 3: # dead and has exactly 3 neighbors
                    board[row][col] = 2 # will live in the next state
                # therefore whatever stayed as 1 will die in the next state

        for row in range(m):
            for col in range(n):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1

    def count_neighbors(self, r, c, mat):
        nei = 0
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                if mat[nr][nc] in [1, 3]:
                    nei += 1

        return nei
