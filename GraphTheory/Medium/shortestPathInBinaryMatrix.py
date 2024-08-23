"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque([[0, 0]])
        grid[0][0] = 1
        steps = 0

        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if x == y == n - 1:
                    return steps + 1
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if self.is_valid(nx, ny, n) and grid[nx][ny] == 0:
                        q.append([nx, ny])
                        grid[nx][ny] = 1
            steps += 1

        return -1

    def is_valid(self, x, y, n):
        return 0 <= x < n and 0 <= y < n
