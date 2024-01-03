"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Link: https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        self.solve(n)
        return self.dp[n]

    def solve(self, n):
        if n <= 1:
            self.dp[n] = 1
            return 1

        if self.dp[n] != -1:
            return self.dp[n]

        one = self.solve(n - 1)
        two = self.solve(n - 2)

        self.dp[n] = one + two

        return self.dp[n]
