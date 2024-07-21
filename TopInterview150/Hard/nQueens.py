"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.solutions = []
        self.cols = set()
        self.diag = set()
        self.anti_diag = set()
        board = [["." for j in range(n)] for i in range(n)]

        self.solve(board, 0)
        return self.solutions

    def solve(self, board, row):
        if row >= self.n:
            return self.solutions.append(["".join(row) for row in board])

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


if __name__ == "__main__":
    s = Solution().solveNQueens(4)

    for sol in s:
        print(sol)
