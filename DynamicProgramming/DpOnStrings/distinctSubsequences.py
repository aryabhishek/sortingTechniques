class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1  # j == 0 means we've already found t in s

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    # take current char coz it's equal
                    dp[i][j] = dp[i - 1][j - 1]
                    # look for other starting matches
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


class Solution: # space optimization 1
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        prev, cur = [], []
        for i in range(m + 1):
            if i != 0:
                prev.append(0)
                cur.append(0)
            else:
                prev.append(1)
                cur.append(1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    cur[j] = prev[j - 1] + prev[j]
                else:
                    cur[j] = prev[j]
            prev = cur.copy()

        return prev[m]
    
class Solution: # ultimate optimization
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [0 if i != 0 else 1 for i in range(m + 1)]

        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = dp[j-1] + dp[j]

        return dp[m]