from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 == 0:

            dp = [[-1] * (s // 2 + 1) for i in range(len(nums))]

            return self.solve(len(nums) - 1, s // 2, nums, dp)

        return False

    def solve(self, ind, target, arr, dp):
        if target == 0:
            return True

        if ind == 0:
            return arr[0] == target

        if dp[ind][target] != -1:
            return dp[ind][target]

        notTaken = self.solve(ind - 1, target, arr, dp)

        taken = False
        if arr[ind] <= target:
            taken = self.solve(ind - 1, target - arr[ind], arr, dp)

        dp[ind][target] = notTaken or taken
        return dp[ind][target]


