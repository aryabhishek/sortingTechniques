from typing import List


def f(idx, w, profit_arr, weight_arr, dp):
    if dp[idx][w] != -1:
        return dp[idx][w]

    if idx == 0:
        # we can steal the curr item any number of times
        return w // weight_arr[0] * profit_arr[0]

    skip = f(idx - 1, w, profit_arr, weight_arr, dp)
    take = 0
    if weight_arr[idx] <= w:
        take = profit_arr[idx] + f(idx, w - weight_arr[idx], profit_arr, weight_arr, dp)

    dp[idx][w] = max(skip, take)
    return dp[idx][w]


def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    cache = [[-1] * (w + 1) for i in range(n)]
    return f(n - 1, w, profit, weight, cache)
