"""
Given an integer array nums and an integer k, 
return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Link: https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if n < 2 or not k:
            return False

        mp = {nums[0]}

        i, j = 0, 1

        while j < n:
            if j - i > k:
                mp.discard(nums[i])
                i += 1
                continue
            if nums[j] in mp:
                return True

            else:
                mp.add(nums[j])
            j += 1

        return False
