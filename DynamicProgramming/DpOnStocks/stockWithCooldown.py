from typing import List

class Solution:
    def solve(self, idx, can_buy, prices, n, dp):
        if idx >= n:
            return 0

        if dp[idx][can_buy]:
            return dp[idx][can_buy]

        if can_buy:
            buy = self.solve(idx + 1, False, prices, n, dp) - prices[idx]
            wait = self.solve(idx + 1, True, prices, n, dp)
            dp[idx][can_buy] = max(buy, wait)
            return dp[idx][can_buy]

        buy = self.solve(idx + 2, True, prices, n, dp) + prices[idx]
        wait = self.solve(idx + 1, False, prices, n, dp)

        dp[idx][can_buy] = max(buy, wait)
        return dp[idx][can_buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        return self.solve(0, True, prices, n, dp)