from typing import List


class Solution:  # memo got TLE
    def solve(self, idx, can_buy, prices, n, dp):
        if idx == n:
            return 0

        if dp[idx][can_buy]:
            return dp[idx][can_buy]

        if can_buy:
            buy = self.solve(idx + 1, False, prices, n, dp) - prices[idx]
            wait = self.solve(idx + 1, True, prices, n, dp)
            dp[idx][can_buy] = max(buy, wait)
            return dp[idx][can_buy]

        buy = self.solve(idx + 1, True, prices, n, dp) + prices[idx]
        wait = self.solve(idx + 1, False, prices, n, dp)

        dp[idx][can_buy] = max(buy, wait)
        return dp[idx][can_buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        return self.solve(0, True, prices, n, dp)


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n + 1)]

        # base case
        dp[n][0] = dp[n][1] = 0

        for idx in range(n - 1, 0, -1):
            for can_buy in range(1, -1, -1):
                if can_buy:
                    buy = dp[idx + 1][0] - prices[idx]
                    wait = dp[idx + 1][1]
                else:
                    buy = dp[idx + 1][1] + prices[idx]
                    wait = dp[idx + 1][0]

                dp[idx][can_buy] = max(buy, wait)

        return dp[0][1]


class Solution: #

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1, -1] for _ in range(n + 1)]

        dp[n][0] = dp[n][1] = 0

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0

                if buy == 0:
                    profit = max(dp[ind + 1][0], -prices[ind] + dp[ind + 1][1])
                else:
                    profit = max(dp[ind + 1][1], prices[ind] + dp[ind + 1][0])

                dp[ind][buy] = profit

        return dp[0][0]


class Solution: # Greedy

    def maxProfit(self, prices: List[int]) -> int:
        p, ans = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] >= p:
                ans += prices[i] - p
            p = prices[i]

        return ans