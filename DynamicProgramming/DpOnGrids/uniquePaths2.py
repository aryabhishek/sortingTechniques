class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        self.map = obstacleGrid
        n = len(self.map)
        m = len(self.map[0])
        self.memo = [[-1]*m for i in range(n)]
        return self.solve(0, 0, n-1, m-1)

    def solve(self, i, j, row, col):

        if i > row or j > col or self.map[i][j] == 1:
            return 0

        if i == row and col == j:
            return 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        right = self.solve(i, j+1, row, col)
        down = self.solve(i+1, j, row, col)

        self.memo[i][j] = right + down

        return self.memo[i][j]
