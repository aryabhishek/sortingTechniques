class Solution:

    def solve(self, idx, heights, memo):
        if idx == 0:
            return 0

        if memo[idx] != -1:
            return memo[idx]

        left = self.solve(idx-1, heights, memo) + abs(heights[idx] - heights[idx-1])
        right = float("inf")

        if idx > 1:
            right = self.solve(idx-2, heights, memo) + abs(heights[idx] - heights[idx-2])

        memo[idx] = min(left, right)

        return memo[idx]

    
    def frogJump(self, n: int, heights: list[int]) -> int:

        # Write your code here.
        dp = [-1]*(n+1)

        return self.solve(n-1, heights, dp)
