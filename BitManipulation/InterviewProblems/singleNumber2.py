"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List


class Solution: # Not good O(n * 32)
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for bit_idx in range(32):
            count = 0
            for num in nums:
                if num & (1 << bit_idx):  # check if bit is set or not
                    count += 1
            if count % 3 == 1:
                ans |= 1 << bit_idx  # set this bit

        # handling negative numbers
        if ans >= 2**31:
            ans -= 2**32

        return ans


class SortingSolution: # O(n*log(n))
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()

        for idx in range(1, len(nums), 3):
            if nums[idx] != nums[idx-1]:
                return nums[idx-1]
        return nums[-1]
    
class BestSolution: # TC: O(n) SC: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0

        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        
        return one