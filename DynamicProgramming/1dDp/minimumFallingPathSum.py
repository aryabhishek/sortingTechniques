class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int: # TLE
        self.n = len(matrix)
        self.mat = matrix

        self.dp = [[-1]*self.n for i in range(self.n)]
        mini = float("inf")
        for i in range(self.n):
            mini = min(mini, self.solve(0, i))

        return mini

    def solve(self, i, j):

        if j < 0 or j >= self.n:
            return float('inf')

        if i == self.n-1:
            return self.mat[i][j]

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        down = self.mat[i][j] + self.solve(i+1, j)
        right_diagonal = self.mat[i][j] + self.solve(i+1, j+1)
        left_diagonal = self.mat[i][j] + self.solve(i+1, j-1)

        self.dp[i][j] = min(down, left_diagonal, right_diagonal)
        return self.dp[i][j]

