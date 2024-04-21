def solve(day, last, points, dp):

    if dp[day][last] != -1:
        return dp[day][last]

    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, points[0][i])
        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0

    for i in range(3):
        if i != last:
            point = points[day][i] + solve(day - 1, i, points, dp)
            maxi = max(maxi, point)

    dp[day][last] = maxi
    return dp[day][last]


def ninjaTraining(n: int, points: list[list[int]]) -> int:

    # Write your code here.
    dp = [[-1]*4 for i in range(n)]

    return solve(n - 1, 3, points, dp)
