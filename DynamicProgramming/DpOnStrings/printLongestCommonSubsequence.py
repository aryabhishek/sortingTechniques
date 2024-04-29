from collections import deque
from sys import stdin


def lcs(s, t):
    # Your code goes here
    n = len(s)
    m = len(t)
    dp = [[-1] * (m + 1) for i in range(n + 1)]

    # base case
    for j in range(m + 1):
        dp[0][j] = 0
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    ans = deque()

    while i > 0 and j > 0:
        left = dp[i][j - 1]
        up = dp[i - 1][j]
        if s[i - 1] == t[j - 1]:
            ans.appendleft(s[i - 1])
            i -= 1
            j -= 1

        elif left > up:
            j -= 1

        else:
            i -= 1

    return "".join(ans)
