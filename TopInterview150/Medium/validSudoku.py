"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
Link: https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            temp = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in temp:
                    return False
                temp.add(board[i][j])

        for i in range(9):
            temp = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in temp:
                    return False
                temp.add(board[j][i])

        for i in range(0, 9, 3):
            end_row = i + 2
            for j in range(0, 9, 3):
                end_col = j + 2
                if not self.valid_box(i, j, end_row, end_col, board):
                    return False

        return True

    def valid_box(self, sr, sc, er, ec, mat) -> bool:
        temp = set()
        for i in range(sr, er + 1):
            for j in range(sc, ec + 1):
                if mat[i][j] == ".":
                    continue
                if mat[i][j] in temp:
                    return False
                temp.add(mat[i][j])

        return True
