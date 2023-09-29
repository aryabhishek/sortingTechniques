class Solution:
    def solve(self, idx, k, heights, memo):
        if idx == 0:
            return 0

        if memo[idx] != -1:
            return memo[idx]


        min_steps = float("inf")

        for i in range(1, k+1):
            if idx - i >= 0:
                jump = self.solve(idx-i, k, heights, memo) + abs(heights[idx] - heights[idx-i])
                min_steps = min(min_steps, jump)

        memo[idx] = min_steps
        return memo[idx]


    def minimizeCost(self, n: int, k: int, heights: list[int]) -> int:
        # Write your code here.
        dp = [-1]*n

        return self.solve(n-1, k, heights, dp)