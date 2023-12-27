"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def max_profit(self, prices: list[int]) -> int:  # DP
        mini = prices[0]
        max_profit = 0

        n = len(prices)

        for i in range(1, n):
            cost = prices[i] - mini
            max_profit = max(max_profit, cost)
            mini = min(mini, prices[i])

        return max_profit

    def maxProfit(self, prices: list[int]) -> int:  # Two-Pointer
        l, r = 0, 1
        ans = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                ans = max(ans, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return ans