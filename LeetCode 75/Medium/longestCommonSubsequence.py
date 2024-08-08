"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

https://leetcode.com/problems/longest-common-subsequence
"""


class Solution:
    def solve(self, i, j, t1, t2, cache):
        if cache[i][j] != -1:
            return cache[i][j]

        if i < 0 or j < 0:
            return 0

        if t1[i] == t2[j]:
            cache[i][j] = 1 + self.solve(i - 1, j - 1, t1, t2, cache)
            return cache[i][j]

        cache[i][j] = max(
            self.solve(i - 1, j, t1, t2, cache), self.solve(i, j - 1, t1, t2, cache)
        )

        return cache[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for i in range(n)]
        res = self.solve(n - 1, m - 1, text1, text2, dp)
        print(dp)
        return res
