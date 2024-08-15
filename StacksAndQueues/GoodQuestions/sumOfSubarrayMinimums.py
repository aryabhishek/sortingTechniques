"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

https://leetcode.com/problems/sum-of-subarray-minimums/
"""

from typing import List
from collections import deque


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        def nearest_smaller_to_left(arr):
            stk = deque()
            res = []

            for i in range(len(arr)):
                ele = arr[i]

                while stk and arr[stk[-1]] >= ele:
                    stk.pop()

                if not stk:
                    res.append(-1)

                else:
                    res.append(stk[-1])

                stk.append(i)

            return res

        def nearest_smaller_to_right(arr):
            stk = deque()
            res = []

            for i in range(len(arr) - 1, -1, -1):
                ele = arr[i]

                while stk and arr[stk[-1]] > ele:
                    stk.pop()

                if not stk:
                    res.append(n)

                else:
                    res.append(stk[-1])

                stk.append(i)
            res.reverse()
            return res

        left = nearest_smaller_to_left(arr)
        right = nearest_smaller_to_right(arr)
        ans = 0
        for i in range(n):
            nsl = left[i]
            nsr = right[i]
            y = nsr - i
            x = i - nsl
            ans += arr[i] * x * y
        return ans % MOD
