from typing import List


class Solution:  # memo

    def solve(self, idx, prev, nums, n, dp):
        if idx == n:
            return 0

        if dp[idx][prev] != -1:
            return dp[idx][prev]

        skip = self.solve(idx + 1, prev, nums, n, dp)
        take = 0
        if prev == -1 or nums[prev] < nums[idx]:
            take = 1 + self.solve(idx + 1, idx, nums, n, dp)

        dp[idx][prev] = max(take, skip)

        return dp[idx][prev]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * n for i in range(n)]
        return self.solve(0, -1, nums, n, dp)


