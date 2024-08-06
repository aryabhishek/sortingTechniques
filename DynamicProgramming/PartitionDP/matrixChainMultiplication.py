"""

"""

from os import *
from sys import *
from collections import *
from math import *


def solve(i, j, array, dp):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    mini = 1e9
    for k in range(i, j):
        steps = (
            array[i - 1] * array[k] * array[j]
            + solve(i, k, array, dp)
            + solve(k + 1, j, array, dp)
        )

        mini = min(mini, steps)

    dp[i][j] = mini
    return mini


def matrixMultiplication(arr, n):
    # Write your code here.
    dp = [[-1] * n for i in range(n)]
    return solve(1, n - 1, arr, dp)


def matrixMultiplicationBottomUp(arr, n):
    # Write your code here.
    dp = [[0] * n for i in range(n)]

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            mini = 1e9
            for k in range(i, j):
                steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]

                mini = min(mini, steps)
            dp[i][j] = mini

    return dp[1][n - 1]
