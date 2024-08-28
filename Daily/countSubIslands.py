"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

https://leetcode.com/problems/count-sub-islands/
"""

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.g1, self.g2 = grid1, grid2
        self.m, self.n = len(grid1), len(grid1[0])
        count = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.g2[i][j] == 1 and self.countSubGrids(i, j):
                    count += 1

        return count

    def countSubGrids(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return True

        if self.g2[i][j] != 1:
            return True

        self.g2[i][j] = -1
        res = self.g1[i][j] == 1

        res &= self.countSubGrids(i, j + 1)
        res &= self.countSubGrids(i, j - 1)
        res &= self.countSubGrids(i + 1, j)
        res &= self.countSubGrids(i - 1, j)

        return res
