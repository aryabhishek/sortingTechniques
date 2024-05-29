class Solution:
    def jump(self, nums: list[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        jumps = 0

        while r < n - 1:
            max_reach = 0
            for i in range(l, r + 1):
                max_reach = max(max_reach, i + nums[i])
            l = r + 1
            r = max_reach
            jumps += 1

        return jumps
