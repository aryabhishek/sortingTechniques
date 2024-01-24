"""

"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(arr, x):
            n = len(arr)
            l = 0
            r = n - 1

            ans = n

            while l <= r:
                m = (l + r) // 2

                if arr[m] >= x:
                    ans = m
                    r = m - 1

                elif arr[m] < x:
                    l = m + 1

            return ans

        def upper_bound(arr, x):
            n = len(arr)
            l = 0
            r = n - 1

            ans = n

            while l <= r:
                m = (l + r) // 2

                if arr[m] > x:
                    ans = m
                    r = m - 1

                elif arr[m] <= x:
                    l = m + 1

            return ans

        lb = lower_bound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        return lb, upper_bound(nums, target) - 1
