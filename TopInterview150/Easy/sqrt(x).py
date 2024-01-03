"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.\=
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Link: https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x

        while True:
            mid = l + (r - l) // 2

            if mid**2 < x:
                l = mid
            elif mid**2 > x:
                r = mid
            if mid**2 <= x < (mid + 1) ** 2:
                return mid
