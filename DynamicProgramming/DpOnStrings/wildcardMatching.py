class Solution:  # memo got TLE
    def solve(self, i, j, s, p, dp):
        if i < 0 and j < 0:
            return True
        if i < 0:
            return False
        if j < 0:
            for itr in range(i + 1):
                if p[itr] != "*":
                    return False
            return True
        if dp[i][j]:
            return dp[i][j]

        if p[i] == s[j] or p[i] == "?":
            dp[i][j] = self.solve(i - 1, j - 1, s, p, dp)
            return dp[i][j]

        elif p[i] == "*":
            dp[i][j] = self.solve(i - 1, j, s, p, dp) or self.solve(i, j - 1, s, p, dp)
            return dp[i][j]

        return False

    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(p), len(s)
        dp = [[False] * (m + 1) for i in range(n)]
        return self.solve(n - 1, m - 1, s, p, dp)


class Solution:  # tabulation

    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(p), len(s)
        dp = [[False] * (m + 1) for i in range(n + 1)]

        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            flag = True
            for itr in range(i):
                if p[itr] != "*":
                    flag = False
                    break
            dp[i][0] = flag

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[n][m]


class Solution: # space optimized

    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(p), len(s)
        prev, cur = [0] * (m + 1), [0] * (m + 1)

        prev[0] = True
        for j in range(1, m + 1):
            prev[j] = False

        for i in range(1, n + 1):
            flag = True
            for itr in range(i):
                if p[itr] != "*":
                    flag = False
                    break
            cur[0] = flag

            for j in range(1, m + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    cur[j] = prev[j - 1]
                elif p[i - 1] == "*":
                    cur[j] = prev[j] or cur[j - 1]
                else:
                    cur[j] = False

            prev = cur.copy()

        return prev[m]
