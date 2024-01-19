"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


class Solution:
    def search(self, arr: list[int], k: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] == k:
                return m

            elif arr[l] <= arr[m]:
                if arr[l] <= k <= arr[m]:
                    r = m - 1

                else:
                    l = m + 1

            else:
                if arr[m] <= k <= arr[r]:
                    l = m + 1

                else:
                    r = m - 1

        return -1
