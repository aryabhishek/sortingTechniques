class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [-1]*(n+1)
        self.solve(n)
        return self.dp[n]

    def solve(self, n):
        if n <= 1:
            self.dp[n] = 1
            return 1

        if self.dp[n] != -1:
            return self.dp[n]

        one = self.solve(n-1)
        two = self.solve(n-2)

        self.dp[n] = one + two

        return self.dp[n]
