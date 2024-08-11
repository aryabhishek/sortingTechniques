"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

https://leetcode.com/problems/count-square-submatrices-with-all-ones/
"""


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

                ans += dp[i][j]

        return ans
