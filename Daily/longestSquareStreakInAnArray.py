"""
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

link: https://leetcode.com/problems/longest-square-streak-in-an-array/
"""


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums.sort()
        ans = -1

        for i in range(len(nums)):
            last = nums[i]
            count = 1

            while self.bs(i + 1, len(nums) - 1, nums, last * last) != -1:
                count += 1
                last *= last
            ans = max(ans, count)

        return ans if ans > 1 else -1

    def bs(self, i, j, nums, target):
        low = i
        high = j
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

