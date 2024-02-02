"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Link: https://leetcode.com/problems/unique-paths-ii
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        self.map = obstacleGrid
        n = len(self.map)
        m = len(self.map[0])
        self.memo = [[-1] * m for i in range(n)]
        return self.solve(0, 0, n - 1, m - 1)

    def solve(self, i, j, row, col):
        if i > row or j > col or self.map[i][j] == 1:  # obstacle encountered
            return 0

        if i == row and col == j: # reached
            return 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        right = self.solve(i, j + 1, row, col)
        down = self.solve(i + 1, j, row, col)

        self.memo[i][j] = right + down

        return self.memo[i][j]
