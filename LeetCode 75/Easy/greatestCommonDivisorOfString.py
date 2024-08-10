"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        def is_divisor(length):
            if m % length == 1 or n % length == 1:
                return False  # doesn't divide evenly so can't make the whole string
            f1, f2 = m // length, n // length
            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for length in range(min(m, n), 0, -1):
            if is_divisor(length):
                return str1[:length]
        return ""


class OptimizedSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if (str1 + str2) == (str2 + str1):
            lengthOfCommonString = math.gcd(len(str1), len(str2))
            return str1[0:lengthOfCommonString]

        return ""
