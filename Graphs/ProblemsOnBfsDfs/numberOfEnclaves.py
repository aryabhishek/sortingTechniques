class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        
        self.n = len(grid)
        self.m = len(grid[0])

        self.vis = [[0]*self.m for _ in range(self.n)]

        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

        count = 0

        for i in range(self.n):
            
            if self.vis[i][0] == 0 and grid[i][0] == 1:
                self.dfs(i, 0, grid)

            if self.vis[i][self.m-1] == 0 and grid[i][self.m-1] == 1:
                self.dfs(i, self.m-1, grid)

        for j in range(self.m):

            if self.vis[0][j] == 0 and grid[0][j] == 1:
                self.dfs(0, j, grid)

            if self.vis[self.n-1][j] == 0 and grid[self.n-1][j] == 1:
                self.dfs(self.n-1, j, grid)

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1 and self.vis[i][j] == 0:
                    count += 1

        return count

    def dfs(self, row, col, mat):
        self.vis[row][col] = 1

        for i in range(4):
            n_row = row + self.dx[i]
            n_col = col + self.dy[i]

            if 0 <= n_row < self.n and 0 <= n_col < self.m and self.vis[n_row][n_col] == 0 and mat[n_row][n_col] == 1:
                self.dfs(n_row, n_col, mat)
