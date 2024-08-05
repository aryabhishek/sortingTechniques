"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

https://leetcode.com/problems/nearest-exit-from-entrance-in-maze
"""

from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        q = deque([[entrance[0], entrance[1], 0]])

        maze[entrance[0]][entrance[1]] = "+"

        while q:
            xo, yo, steps = q.popleft()

            if (0 in [xo, yo] or xo == m - 1 or yo == n - 1) and [xo, yo] != entrance:
                return steps

            for xn, yn in directions:
                x, y = xo + xn, yo + yn
                if 0 <= x < m and 0 <= y < n and maze[x][y] == ".":
                    maze[x][y] = "+"
                    q.append([x, y, steps + 1])

        return -1
