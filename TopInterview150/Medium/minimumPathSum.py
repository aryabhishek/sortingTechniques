"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
Link: https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        self.grid = grid

        n = len(self.grid)
        m = len(self.grid[0])
        self.memo = [[-1] * m for i in range(n)]
        return self.solve(0, 0, n - 1, m - 1)

    def solve(self, i, j, row, col):
        if i == row and j == col:
            return self.grid[i][j]

        if i > row or j > col:
            return float("inf")

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        right = self.grid[i][j] + self.solve(i, j + 1, row, col)
        down = self.grid[i][j] + self.solve(i + 1, j, row, col)

        self.memo[i][j] = min(right, down)

        return self.memo[i][j]
