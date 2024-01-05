"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Link: https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)

        low = 0
        high = n - 1

        while low <= high:
            mid = (high - low) // 2 + low

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return low
