"""

"""


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]

        dp = [[0] * len(cuts) for _ in range(len(cuts))]

        def solve(i: int, j: int) -> int:
            if i > j:
                return 0

            if dp[i][j] != 0:
                return dp[i][j]

            mini = float("inf")

            for ind in range(i, j + 1):
                cost = cuts[j + 1] - cuts[i - 1] + solve(i, ind - 1) + solve(ind + 1, j)
                mini = min(cost, mini)

            dp[i][j] = mini
            return mini

        return solve(1, len(cuts) - 2)


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        
        dp = [[0] * (m + 2) for _ in range(m + 2)]

        for length in range(2, m + 2):
            for i in range(m + 2 - length):
                j = i + length
                dp[i][j] = float('inf')
                
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
        
        return dp[0][m + 1]