from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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

        if coins[i] > amount: # we skip this coin
            self.memo[i][amount] = self.solve(i+1, coins, amount)
            return self.memo[i][amount]
        # otherwise we still have two options, we can either take it or leave it
        take = self.solve(i, coins, amount-coins[i])
        skip = self.solve(i+1, coins, amount)

        self.memo[i][amount] = take + skip

        return self.memo[i][amount]