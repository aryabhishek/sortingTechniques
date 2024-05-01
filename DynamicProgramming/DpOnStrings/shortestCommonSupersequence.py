from collections import deque


class Solution:
    def modified_lcs(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for i in range(n + 1)]

        # base case
        for j in range(m + 1):
            dp[0][j] = 0
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = n, m
        q = deque()

        while i > 0 and j > 0:
            left = dp[i][j - 1]
            up = dp[i - 1][j]
            if text1[i - 1] == text2[j - 1]:
                q.appendleft(text1[i - 1])
                i -= 1
                j -= 1
            elif left > up:
                q.appendleft(text2[j - 1])
                j -= 1
            else:
                q.appendleft(text1[i - 1])
                i -= 1

        while i > 0:
            q.appendleft(text1[i - 1])
            i -= 1

        while j > 0:
            q.appendleft(text2[j - 1])
            j -= 1

        return "".join(q)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        return self.modified_lcs(str1, str2)
