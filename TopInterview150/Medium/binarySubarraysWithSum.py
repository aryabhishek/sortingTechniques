"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
"""


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def find(arr, target):
            if target < 0:
                return 0
            n = len(nums)
            start = ans = total = 0

            for end in range(n):
                total += nums[end]

                while total > target:
                    total -= nums[start]
                    start += 1
                ans += end - start + 1

            return ans

        return find(nums, goal) - find(nums, goal - 1)
