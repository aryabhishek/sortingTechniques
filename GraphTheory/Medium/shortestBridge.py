"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

https://leetcode.com/problems/shortest-bridge/
"""

from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        vis = set()

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in vis:
                return
            vis.add((r, c))

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(vis)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        cur_r, cur_c = r + dr, c + dc
                        if invalid(cur_r, cur_c) or (cur_r, cur_c) in vis:
                            continue
                        if grid[cur_r][cur_c]:
                            return res
                        q.append([cur_r, cur_c])
                        vis.add((cur_r, cur_c))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
