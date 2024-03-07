"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.
Link: https://leetcode.com/problems/coin-change-ii/
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        self.n = len(coins)
        self.memo = [[-1] * (amount + 1) for i in range(self.n)]
        return self.solve(0, coins, amount)

    def solve(self, i, coins, amount):
        if amount == 0:
            return 1

        if i == self.n:
            return 0

        if self.memo[i][amount] != -1:
            return self.memo[i][amount]

        if coins[i] > amount:
            self.memo[i][amount] = self.solve(i + 1, coins, amount)
            return self.memo[i][amount]

        take = self.solve(i, coins, amount - coins[i])
        skip = self.solve(i + 1, coins, amount)

        self.memo[i][amount] = take + skip

        return self.memo[i][amount]
