def solve(idx, price, n, dp):
    if dp[idx][n] != -1:
        return dp[idx][n]
    if idx == 0:
        return n * price[0]

    skip = solve(idx - 1, price, n, dp)
    take = 0
    rod_length = idx + 1 # 1-based indexing
    if rod_length <= n:
        take = price[idx] + solve(idx, price, n - rod_length, dp)

    dp[idx][n] = max(take, skip)
    return dp[idx][n]


def cutRod(price, n):
    cache = [[-1] * (n + 1) for i in range(n)]
    return solve(n - 1, price, n, cache)
