"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.find(i, j, 0, board, word):
                    return True
        return False

    def find(self, i, j, idx, board, word):
        if idx == len(word):
            return True

        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or board[i][j] == "#"
        ):
            return False

        if board[i][j] != word[idx]:
            return False

        temp = board[i][j]
        board[i][j] = "#"  # mark visited

        for k in range(4):
            r = i + self.dx[k]
            c = j + self.dy[k]
            # look for the next character
            if self.find(r, c, idx + 1, board, word):
                return True
        board[i][j] = temp
        return False
