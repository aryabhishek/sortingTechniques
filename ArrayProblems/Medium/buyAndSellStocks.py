"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def solution(prices: list) -> int: # TC: O(n), SC: O(1)

    mini = prices[0]
    max_profit = 0

    n = len(prices)

    for i in range(1, n):
        cost = prices[i] - mini
        max_profit = max(max_profit, cost)
        mini = min(mini, prices[i])

    return max_profit


if __name__ == "__main__":
    arr = [7,1,5,3,6,4]

    print(solution(arr))
