"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

https://leetcode.com/problems/max-area-of-island/
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.cur_area = 0
        max_area = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.dfs(i, j)
                    max_area = max(self.cur_area, max_area)
                    self.cur_area = 0

        return max_area

    def dfs(self, r, c):
        if r < 0 or r >= self.m or c < 0 or c >= self.n or self.grid[r][c] == 0:
            return

        self.cur_area += 1
        self.grid[r][c] = 0

        self.dfs(r - 1, c)
        self.dfs(r + 1, c)
        self.dfs(r, c - 1)
        self.dfs(r, c + 1)
