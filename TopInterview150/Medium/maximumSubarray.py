"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
Link: https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        total = 0

        for i in range(n):
            total += nums[i]
            ans = max(total, ans)
            if total < 0:
                total = 0

        return ans
