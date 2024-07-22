"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, N = len(s1), len(s2), len(s3)
        if m + n != N:
            return False

        memo = {}

        def solve(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if k == N:
                return True

            result = False
            if i < m and s1[i] == s3[k]:
                result = solve(i + 1, j, k + 1)
            if j < n and s2[j] == s3[k]:
                result = result or solve(i, j + 1, k + 1)

            memo[(i, j, k)] = result
            return result

        return solve(0, 0, 0)
