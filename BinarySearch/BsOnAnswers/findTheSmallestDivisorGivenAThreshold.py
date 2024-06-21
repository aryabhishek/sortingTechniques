"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""

from math import ceil


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def get_sum(arr, divisor):
            return sum(ceil(num / divisor) for num in arr)

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2

            if get_sum(nums, mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1

        return left
