"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

https://leetcode.com/problems/partition-array-for-maximum-sum/
"""


class Solution:
    def maxSumAfterPartitioning(self, num: list[int], k: int) -> int:
        n = len(num)
        dp = [0] * (n + 1)

        for ind in range(n - 1, -1, -1):
            len_val = 0
            max_val = float("-inf")
            max_ans = float("-inf")

            for j in range(ind, min(ind + k, n)):
                len_val += 1
                max_val = max(max_val, num[j])
                summation = len_val * max_val + dp[j + 1]
                max_ans = max(max_ans, summation)

            dp[ind] = max_ans

        return dp[0]
