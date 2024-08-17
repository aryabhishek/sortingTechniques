"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

https://leetcode.com/problems/number-of-closed-islands/
"""


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        islands = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    if self.dfs(i, j):
                        islands += 1

        return islands

    def dfs(self, r, c):
        if r < 0 or r >= self.m or c < 0 or c >= self.n:
            return False

        if self.grid[r][c] == 1:
            return True

        self.grid[r][c] = 1

        up = self.dfs(r - 1, c)
        down = self.dfs(r + 1, c)
        left = self.dfs(r, c - 1)
        right = self.dfs(r, c + 1)

        return up and down and left and right
