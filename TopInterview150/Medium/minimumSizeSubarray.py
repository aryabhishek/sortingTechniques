"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Link: https://leetcode.com/problems/minimum-size-subarray-sum
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = j = total = 0
        ans = float("inf")
        n = len(nums)

        while j < n:
            total += nums[j]

            if total < target:
                j += 1
            else:
                while total >= target:
                    ans = min(ans, j - i + 1)
                    total -= nums[i]
                    i += 1
                j += 1
        return ans if ans != float("inf") else 0
