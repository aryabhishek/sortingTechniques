"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Link: https://leetcode.com/problems/rotate-array
"""


class Solution:
    def optimal_rotation(self, arr, k, n):  # TC: O(2n), SC: O(1)
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(0, n - 1 - k)  # reversing from start to n-k (zero indexed)
        reverse(n - k, n - 1)  # reversing from n-k to end (zero indexed)
        reverse(0, n - 1)  # reversing from start to end

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        self.optimal_rotation(nums, k % n, n)
