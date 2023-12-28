"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Link: https://leetcode.com/problems/two-sum/?envType=study-plan-v2&envId=top-interview-150
"""


# from itertools import permutations
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, val in enumerate(nums):
            rem = target - val

            if rem in seen:
                return i, seen[rem]

            seen[val] = i
