"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
Link: https://leetcode.com/problems/product-of-array-except-self
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [nums[0]]
        suffix = [0] * (n - 1) + [nums[-1]]

        for i in range(1, n):
            prefix.append(prefix[i - 1] * nums[i])
            suffix[n - i - 1] = nums[n - i - 1] * suffix[n - i]

        ans = []

        for i in range(n):
            if i == 0:
                ans.append(suffix[i + 1])
            elif i == n - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * suffix[i + 1])

        return ans
