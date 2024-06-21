"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        i = j = 0

        while j < n:
            if j - i + 1 == m:
                if haystack[i : j + 1] == needle:
                    return i
                i += 1
            j += 1
        return -1
