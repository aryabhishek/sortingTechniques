from typing import List


class Solution:
    def solve(self, idx, buy, cap, prices, n, dp):
        if idx == n or cap == 0:
            return 0

        if dp[idx][buy][cap] != -1:
            return dp[idx][buy][cap]

        if buy:
            dp[idx][buy][cap] = max(
                self.solve(idx + 1, 0, cap, prices, n, dp) - prices[idx],
                self.solve(idx + 1, 1, cap, prices, n, dp),
            )
            return dp[idx][buy][cap]

        dp[idx][buy][cap] = max(
            self.solve(idx + 1, 1, cap - 1, prices, n, dp) + prices[idx],
            self.solve(idx + 1, 0, cap, prices, n, dp),
        )
        return dp[idx][buy][cap]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1] * 3 for i in range(2)] for i in range(n)]
        return self.solve(0, 1, 2, prices, n, dp)


