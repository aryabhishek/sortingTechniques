"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

https://leetcode.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1] * n for i in range(m)]
        return self.solve(0, 0, m - 1, n - 1)

    def solve(self, i, j, row, col):
        if i == row and col == j:
            return 1

        if i > row or j > col:
            return 0

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        right = self.solve(i, j + 1, row, col)
        down = self.solve(i + 1, j, row, col)

        self.memo[i][j] = right + down

        return self.memo[i][j]
