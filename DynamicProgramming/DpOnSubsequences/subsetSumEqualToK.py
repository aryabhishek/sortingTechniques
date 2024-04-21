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
    dp = [[-1] * (k + 1) for i in range(n)]

    return solve(n - 1, k, arr, dp)


def subsetSumToK(n, k, arr): # tablulation approach
    dp = [[0] * (k + 1) for i in range(n)]

    for i in range(n):
        dp[i][0] = 1  # target 0 can always be achieved

    if arr[0] <= k:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for target in range(1, k + 1):
            not_taken = dp[i - 1][target]  # target stays the same
            taken = 0
            if arr[i] <= target:
                taken = dp[i - 1][target - arr[i]]

            dp[i][target] = taken or not_taken

    return dp[n - 1][k]
