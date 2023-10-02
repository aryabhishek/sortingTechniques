class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1]*n for i in range(m)]
        return self.solve(0, 0, m-1, n-1)

    def solve(self, i, j, row, col):
        if i == row and col == j:
            return 1

        if i > row or j > col:
            return 0

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        right = self.solve(i, j+1, row, col)
        down = self.solve(i+1, j, row, col)

        self.memo[i][j] = right + down

        return self.memo[i][j]
