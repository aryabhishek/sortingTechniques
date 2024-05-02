class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        max_profit = 0

        n = len(prices)

        for i in range(1, n):
            cost = prices[i] - mini
            max_profit = max(max_profit, cost)
            mini = min(mini, prices[i])

        return max_profit
