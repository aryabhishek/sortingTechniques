from typing import List


class Solution:  # memoization gives TLE
    mx = int(1e9)

    def f(self, arr, ind, total, dp):
        if dp[ind][total] != self.mx:
            return dp[ind][total]

        if ind == 0:
            if total % arr[0] == 0:
                return total // arr[0]
            return self.mx

        notTaken = self.f(arr, ind - 1, total, dp)

        taken = self.mx

        if arr[ind] <= total:
            taken = 1 + self.f(arr, ind, total - arr[ind], dp)

        dp[ind][total] = min(taken, notTaken)

        return dp[ind][total]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cache = [[self.mx] * (amount + 1) for i in range(n)]
        ans = self.f(coins, n - 1, amount, cache)
        return ans if ans != self.mx else -1


class Solution: # tabulation
    mx = int(1e9)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        table = [[self.mx] * (amount + 1) for i in range(n)]

        for col in range(amount + 1):
            if col % coins[0] == 0:
                table[0][col] = col // coins[0]

        for row in range(n):
            table[row][0] = 0

        for i in range(1, n):
            for j in range(1, amount + 1):
                notTaken = table[i - 1][j]
                taken = self.mx

                if coins[i] <= j:
                    taken = 1 + table[i][j - coins[i]]

                table[i][j] = min(taken, notTaken)

        ans = table[n - 1][amount]

        return ans if ans != self.mx else -1
