class Solution:  # simple memoization
    def solve(self, i, j, s, t, dp):
        if dp[i][j]:
            return dp[i][j]
        if i < 0:
            return j + 1  # we have to insert j + 1 chars
        if j < 0:
            return i + 1  # we have to delete i + 1 chars

        if s[i] == t[j]:
            dp[i][j] = self.solve(i - 1, j - 1, s, t, dp)
            return dp[i][j]

        ans = 0
        # insert operation
        ans += 1 + self.solve(i, j - 1, s, t, dp)
        # delete operation
        ans = min(ans, 1 + self.solve(i - 1, j, s, t, dp))
        # replace operation
        ans = min(ans, 1 + self.solve(i - 1, j - 1, s, t, dp))

        dp[i][j] = ans
        return ans

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = [[0] * (m + 1) for i in range(n + 1)]
        return self.solve(n - 1, m - 1, word1, word2, cache)


class Solution:  # tabulation

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1] * (m + 1) for i in range(n + 1)]

        # base cases
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        # tabulation
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # insetion
                    dp[i][j] = 1 + dp[i][j - 1]
                    # deletion
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
                    # replacement
                    dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j - 1])

        return dp[n][m]


class Solution:  # space optimized

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev, cur = [], []

        for i in range(m + 1):
            prev.append(i)
            cur.append(0)

        for i in range(1, n + 1):
            cur[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(cur[j - 1], prev[j], prev[j - 1])
            prev = cur.copy()

        return prev[m]
