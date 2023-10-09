
def solve(ind, target, arr, dp):
    if target == 0:
        return True

    if ind == 0:
        return arr[0] == target

    if dp[ind][target] != -1:
        return dp[ind][target]

    notTaken = solve(ind - 1, target, arr, dp)

    taken = False
    if arr[ind] <= target:
        taken = solve(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = notTaken or taken
    return dp[ind][target]


def subsetSumToK(n, k, arr):
    dp = [[-1]*(k + 1) for i in range(n)]

    return solve(n - 1, k, arr, dp)
