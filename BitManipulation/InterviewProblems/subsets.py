"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = 1 << n
        ans = []

        for num in range(subsets):
            subset = []
            for i in range(n):
                if num & (1 << i):  # check if ith bit is set or not
                    subset.append(nums[i])
            ans.append(subset)

        return ans
