"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.solutions = 0
        self.cols = set()
        self.diag = set()
        self.anti_diag = set()
        board = [["." for j in range(n)] for i in range(n)]

        self.solve(board, 0)
        return self.solutions

    def solve(self, board, row):
        if row >= self.n:
            self.solutions += 1
            return

        for col in range(self.n):
            # up = col
            diag = row + col
            anti_diag = row - col
            if col in self.cols or diag in self.diag or anti_diag in self.anti_diag:
                continue

            self.cols.add(col)
            self.diag.add(diag)
            self.anti_diag.add(anti_diag)
            board[row][col] = "Q"

            self.solve(board, row + 1)

            self.cols.discard(col)
            self.diag.discard(diag)
            self.anti_diag.discard(anti_diag)
            board[row][col] = "."
