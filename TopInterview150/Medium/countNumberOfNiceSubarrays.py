"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def find(arr, target):
            if target < 0:
                return 0
            n = len(nums)
            start = ans = odd = 0

            for end in range(n):
                odd += nums[end] % 2

                while odd > target:
                    odd -= nums[start] % 2
                    start += 1
                ans += end - start + 1

            return ans

        return find(nums, k) - find(nums, k - 1)
