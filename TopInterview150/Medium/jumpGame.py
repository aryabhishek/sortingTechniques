"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
Link: https://leetcode.com/problems/jump-game/description
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        maxx = 0

        for i in range(len(nums)-1):

            if nums[i] == maxx == 0: # jumps got exhausted
                return False

            elif nums[i] >= maxx: # check if we can reach nums[i] with our previous jump
                maxx = nums[i]

            maxx -= 1

        return True