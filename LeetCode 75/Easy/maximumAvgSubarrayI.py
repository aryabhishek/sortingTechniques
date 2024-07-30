"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

https://leetcode.com/problems/maximum-average-subarray-i
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        avg = float("-inf")
        cur_sum = 0
        l = r = 0

        while r < n:
            cur_sum += nums[r]

            if r - l + 1 == k:
                avg = max(avg, cur_sum / k)
                cur_sum -= nums[l]
                l += 1

            r += 1

        return avg
