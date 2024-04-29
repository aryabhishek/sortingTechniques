class Solution: # memoization
    def solve(self, i, j, t1, t2, cache):
        if cache[i][j] != -1:
            return cache[i][j]

        if i < 0 or j < 0:
            return 0

        if t1[i] == t2[j]:
            cache[i][j] = 1 + self.solve(i - 1, j - 1, t1, t2, cache)
            return cache[i][j]

        cache[i][j] = max(
            self.solve(i - 1, j, t1, t2, cache), self.solve(i, j - 1, t1, t2, cache)
        )

        return cache[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for i in range(n)]
        res = self.solve(n - 1, m - 1, text1, text2, dp)
        return res


class Solution: # tabulation

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1]*(m + 1) for i in range(n+1)]
        
        # base case
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]