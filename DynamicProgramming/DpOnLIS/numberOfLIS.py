"""
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.
"""

from typing import List


class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1] * n
        count = [1] * n
        maxi = 1

        for i in range(n):
            for prev in range(i):
                if arr[prev] < arr[i] and dp[prev] + 1 > dp[i]:
                    dp[i] = dp[prev] + 1
                    count[i] = count[prev]
                elif arr[prev] < arr[i] and dp[prev] + 1 == dp[i]:
                    count[i] += count[prev]

            maxi = max(maxi, dp[i])

        ans = 0

        for i in range(n):
            if dp[i] == maxi:
                ans += count[i]

        return ans
