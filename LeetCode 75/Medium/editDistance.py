"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

https://leetcode.com/problems/edit-distance/
"""


class Solution:
    def solve(self, i, j, s, t, dp):
        if dp[i][j]:
            return dp[i][j]
        if i < 0:
            return j + 1  # we have to insert j + 1 chars
        if j < 0:
            return i + 1  # we have to delete i + 1 chars

        if s[i] == t[j]:
            dp[i][j] = self.solve(i - 1, j - 1, s, t, dp)
            return dp[i][j]

        else:
            ans = 0
            # insert operation
            ans += 1 + self.solve(i, j - 1, s, t, dp)
            # delete operation
            ans = min(ans, 1 + self.solve(i - 1, j, s, t, dp))
            # replace operation
            ans = min(ans, 1 + self.solve(i - 1, j - 1, s, t, dp))

            dp[i][j] = ans
            return ans

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = [[0] * (m + 1) for i in range(n + 1)]
        return self.solve(n - 1, m - 1, word1, word2, cache)
