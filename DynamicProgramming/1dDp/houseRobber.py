class Solution:
    def rob(self, nums: list[int]) -> int:
        self.nums = nums

        return self.solve(len(nums)-1)

    def recursion(self, idx):
        if idx == 0:
            return self.nums[idx]

        if idx < 0:
            return 0

        pick = self.nums[idx] + self.solve(idx-2)
        dont_pick = self.solve(idx-1)

        return max(pick, dont_pick)

    def memoised(self, idx):
        # if we come to idx 0 we must've come from 2 that means we can always pick idx 0
        if idx == 0:
            return self.nums[idx]

        if idx < 0:
            return 0

        if self.dp[idx] != -1:  # check if it's already present
            return self.dp[idx]

        # when we pick the current element we can't pick it's neighbour
        pick = self.nums[idx] + self.solve(idx-2)
        # when we don't pick the current element we can pick it's neighbour
        dont_pick = self.solve(idx-1)

        self.dp[idx] = max(pick, dont_pick)  # store it

        return self.dp[idx]

    def space_optimised(self, nums: list[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev = nums[0]

        for i in range(1, n):
            take = nums[i]
            if i > 1:
                take += prev2

            dont_take = prev

            cur = max(take, dont_take)
            prev2 = prev
            prev = cur

        return prev
