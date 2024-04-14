class Solution:

    def dfs(
        self,
        row: int,
        col: int,
        grid: list[int][int],
        vis: list[int][int],
        brow: int,
        bcol: int,
        dist: list,
    ):
        vis[row][col] = 1
        dist.append((row - brow, col - bcol))

        drow = [0, 0, 1, -1]
        dcol = [1, -1, 0, 0]

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if (
                0 <= nrow < self.n
                and 0 <= ncol < self.m
                and grid[nrow][ncol] == 1
                and not vis[nrow][ncol]
            ):
                self.dfs(nrow, ncol, grid, vis, brow, bcol, dist)

    def countDistinctIslands(self, grid: list[list[int]]) -> int:
        # code here
        self.n = len(grid)
        self.m = len(grid[0])
        vis = [[0] * self.m for i in range(self.n)]
        ans = set()

        for i in range(self.n):
            for j in range(self.m):
                if not vis[i][j] and grid[i][j] == 1:
                    dist = []
                    self.dfs(i, j, grid, vis, i, j, dist)
                    ans.add(tuple(dist))

        return len(ans)
