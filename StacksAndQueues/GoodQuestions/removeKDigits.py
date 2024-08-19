"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

https://leetcode.com/problems/remove-k-digits/
"""

from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        dq = deque()

        for digit in num:
            while dq and k > 0 and dq[-1] > digit:
                dq.pop()
                k -= 1
            dq.append(digit)

        while k > 0:
            dq.pop()
            k -= 1

        while dq and dq[0] == "0":
            dq.popleft()

        return "".join(dq) if dq else "0"
