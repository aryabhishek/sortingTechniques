class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.n = len(board)
        self.m = len(board[0])
        self.vis = [[0]*self.m for _ in range(self.n)]

        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]

        for i in range(self.n):

            if board[i][0] == "O" and self.vis[i][0] == 0:
                self.dfs(i, 0, board)

            if board[i][self.m-1] == "O" and self.vis[i][self.m-1] == 0:
                self.dfs(i, self.m-1, board)

        for j in range(self.m):

            if board[0][j] == "O" and self.vis[0][j] == 0:
                self.dfs(0, j, board)

            if board[self.n-1][j] == "O" and self.vis[self.n-1][j] == 0:
                self.dfs(self.n-1, j, board)

        for i in range(self.n):
            for j in range(self.m):
                if self.vis[i][j] == 0 and board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, row, col, mat):
        self.vis[row][col] = 1

        for i in range(4):
            n_row = row + self.dx[i]
            n_col = col + self.dy[i]

            if 0 <= n_row < self.n and 0 <= n_col < self.m and self.vis[n_row][n_col] == 0 and mat[n_row][n_col] == "O":
                self.dfs(n_row, n_col, mat)
