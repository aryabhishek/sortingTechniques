"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

https://leetcode.com/problems/max-number-of-k-sum-pairs
"""


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        count = 0

        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                count += 1
                l += 1
                r -= 1

            elif total < k:
                l += 1
            
            else:
                r -= 1
        
        return count