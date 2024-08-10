"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

https://leetcode.com/problems/burst-balloons/
"""


class Solution:  # memo
    def maxCoins(self, nums: list[int]) -> int:
        self.nums = [1] + nums + [1]
        self.memo = {}
        return self.solve(1, len(nums))

    def solve(self, i, j):
        if i > j:
            return 0

        if (i, j) in self.memo:
            return self.memo[(i, j)]

        maxi = float("-inf")
        for last in range(i, j + 1):
            cost = (
                self.nums[i - 1] * self.nums[last] * self.nums[j + 1]
                + self.solve(i, last - 1)
                + self.solve(last + 1, j)
            )
            maxi = max(maxi, cost)

        self.memo[(i, j)] = maxi
        return maxi


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue
                maxi = float("-inf")

                for ind in range(i, j + 1):
                    cost = (
                        nums[i - 1] * nums[ind] * nums[j + 1]
                        + dp[i][ind - 1]
                        + dp[ind + 1][j]
                    )
                    maxi = max(maxi, cost)

                dp[i][j] = maxi

        return dp[1][n]
