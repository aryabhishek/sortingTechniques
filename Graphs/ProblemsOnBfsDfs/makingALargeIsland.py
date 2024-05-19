from typing import List
from disjointSet import DisjointSet


class Solution:
    def isValid(self, r, c, n, m):
        return 0 <= r < n and 0 <= c < m

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        ds = DisjointSet(n * n)

        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        for i in range(n * n):
            if grid[i // n][i % n] == 0:
                continue
            for i_dir in range(4):
                nr = i // n + dr[i_dir]
                nc = i % n + dc[i_dir]
                if self.isValid(nr, nc, n, n) and grid[nr][nc] == 1:
                    ds.union_by_size(i, nr * n + nc)

        mx = 0
        for i in range(n * n):
            if grid[i // n][i % n] == 1:
                continue
            components = set()
            for i_dir in range(4):
                nr = i // n + dr[i_dir]
                nc = i % n + dc[i_dir]
                if self.isValid(nr, nc, n, n) and grid[nr][nc] == 1:
                    components.add(ds.find_ultimate_parent(nr * n + nc))

            total_size = 0
            for component in components:
                total_size += ds.size[component]

            mx = max(
                mx, total_size + 1
            )  # added 1 for the 0 that we just converted to 1

        for i in range(n * n):
            mx = max(mx, ds.size[ds.find_ultimate_parent(i)])

        return mx
