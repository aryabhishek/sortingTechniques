"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Link: https://leetcode.com/problems/find-peak-element
"""


class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        elif arr[0] > arr[1]:
            return 0

        elif arr[-1] > arr[-2]:
            return n - 1

        low, high = 1, n - 2

        while low <= high:

            mid = (high - low) // 2 + low

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid

            elif arr[mid] > arr[mid - 1]:  # peak is on the right side
                low = mid + 1

            else:  # peak is on the left side
                high = mid - 1

        return -1
