"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

https://leetcode.com/problems/next-greater-element-ii/
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        nge = [-1] * n

        for i in range(2 * n - 1, -1, -1):
            idx = i % n

            while stack and stack[-1] <= nums[idx]:
                stack.pop()

            if i < n and stack:
                nge[i] = stack[-1]

            stack.append(nums[idx])

        return nge
