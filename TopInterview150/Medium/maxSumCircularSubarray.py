"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        max_sum = self.max_subarray_sum(nums)
        min_sum = self.min_subarray_sum(nums)
        max_circular_sum = total - min_sum

        if max_sum > 0:
            return max(max_sum, max_circular_sum)
        return max_sum

    def min_subarray_sum(self, nums):
        n = len(nums)
        min_sum = total = nums[0]

        for i in range(1, n):
            total = min(total + nums[i], nums[i])
            min_sum = min(min_sum, total)

        return min_sum

    def max_subarray_sum(self, nums):
        n = len(nums)
        max_sum = total = nums[0]

        for i in range(1, n):
            total = max(total + nums[i], nums[i])
            max_sum = max(max_sum, total)

        return max_sum
