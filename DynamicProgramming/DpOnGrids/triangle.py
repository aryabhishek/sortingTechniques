class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        self.n = len(triangle)
        self.triangle = triangle

        self.dp = [[-1 for j in range(1, self.n)] for i in range(self.n)]
        return self.solve(0, 0)

    def solve(self, i, j):

        if i == self.n-1:
            return self.triangle[i][j]

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        down = self.triangle[i][j] + self.solve(i+1, j)
        diagonal = self.triangle[i][j] + self.solve(i+1, j+1)

        self.dp[i][j] = min(down, diagonal)
        return self.dp[i][j]
