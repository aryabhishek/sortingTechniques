"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).

Link: https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1

        return l == len(s)
