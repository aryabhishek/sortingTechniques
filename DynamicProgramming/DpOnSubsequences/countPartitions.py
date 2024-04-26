from typing import List


def f(arr, idx, target, memo):
    if memo[idx][target] != -1:
        return memo[idx][target]

    if target == 0:
        return 1

    if idx == 0:
        if target == arr[idx]:
            return 1
        return 0

    not_picked = f(arr, idx - 1, target, memo)
    picked = 0
    if arr[idx] <= target:
        picked = f(arr, idx - 1, target - arr[idx], memo)

    memo[idx][target] = picked + not_picked
    return picked + not_picked


def findWays(nums: List[int], k: int) -> int:
    n = len(nums)
    memo = [[-1] * (k + 1) for _ in range(n)]

    return f(nums, n - 1, k, memo)


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    total = sum(arr)
    if (total - d) < 0 or (total - d) % 2:
        return 0
    return findWays(arr, (total - d) // 2)
