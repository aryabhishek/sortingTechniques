"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

https://leetcode.com/problems/house-robber
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        self.nums = nums
        self.dp = [-1] * (len(nums) + 1)

        return self.solve(len(nums) - 1)

    def solve(self, idx):
        # if we come to idx 0 we must've come from 2 that means we can always pick idx 0
        if idx == 0:
            return self.nums[idx]

        if idx < 0:
            return 0

        if self.dp[idx] != -1:  # check if it's already present
            return self.dp[idx]

        # when we pick the current element we can't pick it's neighbour
        pick = self.nums[idx] + self.solve(idx - 2)
        # when we don't pick the current element we can pick it's neighbour
        dont_pick = self.solve(idx - 1)

        self.dp[idx] = max(pick, dont_pick)  # store it

        return self.dp[idx]
