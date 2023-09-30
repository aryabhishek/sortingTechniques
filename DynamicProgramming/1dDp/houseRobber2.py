class Solution:
    def rob(self, arr: list[int]) -> int:
        return arr[0] if len(arr) == 1 else max(self.rob_houses(arr[:-1]), self.rob_houses(arr[1:]))
        
    def rob_houses(self, nums: list[int]) -> int:
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